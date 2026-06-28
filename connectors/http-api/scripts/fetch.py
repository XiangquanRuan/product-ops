#!/usr/bin/env python3
"""
HTTP API Data Connector for product-ops.

Fetches operational data from any REST API by reading a connector config
that defines the endpoint, auth, and field mappings.

Usage:
    python fetch.py --config <path> --workflow <name> --start <date> --end <date>

Input:  Connector config JSON + CLI args
Output: DataResponse JSON (standard product-ops format)
"""

import argparse
import json
import os
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print(json.dumps({
        "status": "failed",
        "source": "http-api",
        "source_detail": "Python requests library not installed",
        "period": {},
        "fetched_at": datetime.now().isoformat(),
        "metrics": {},
        "anomalies": [],
        "warnings": ["Install requests: pip install requests"]
    }, ensure_ascii=False, indent=2))
    sys.exit(1)


def load_config(config_path: str) -> dict:
    """Load connector config from JSON file."""
    config_path = os.path.expanduser(config_path)
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_request(config: dict, start_date: str, end_date: str) -> tuple:
    """Build HTTP request from config and date range."""
    endpoint = config["endpoints"]["metrics"]
    method = endpoint.get("method", "GET").upper()
    url = config["base_url"].rstrip("/") + "/" + endpoint["path"].lstrip("/")

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    # Auth
    auth_type = config.get("auth", {}).get("type", "bearer")
    auth_config = config.get("auth", {})
    if auth_type == "bearer":
        headers["Authorization"] = f"Bearer {auth_config['key']}"
    elif auth_type == "basic":
        auth = (auth_config["key"], auth_config["secret"])
    elif auth_type == "header":
        headers[auth_config["header_name"]] = auth_config["key"]
        auth = None
    elif auth_type == "query":
        url += f"?{auth_config['query_param']}={auth_config['key']}"
        auth = None
    else:
        auth = None

    # Body
    body = None
    if method == "POST" and "body_template" in endpoint:
        import re
        body_str = json.dumps(endpoint["body_template"])
        body_str = body_str.replace("{{start_date}}", start_date)
        body_str = body_str.replace("{{end_date}}", end_date)
        body = json.loads(body_str)

    return method, url, headers, auth, body


def extract_value(response_json: dict, jsonpath: str) -> any:
    """Extract a value from JSON using dot/bracket notation path."""
    parts = jsonpath.replace("[", ".").replace("]", "").split(".")
    current = response_json
    for part in parts:
        if part == "":
            continue
        if isinstance(current, list):
            try:
                current = current[int(part)]
            except (IndexError, ValueError):
                return None
        elif isinstance(current, dict):
            current = current.get(part)
            if current is None:
                return None
        else:
            return None
    return current


def transform_value(raw: any, mapping: dict) -> float | None:
    """Apply type conversion and transforms."""
    if raw is None:
        return None

    try:
        value = float(raw)
    except (ValueError, TypeError):
        return None

    transform = mapping.get("transform", "none")
    if transform == "divide_by_100":
        value = value / 100.0
    elif transform == "multiply_by_100":
        value = value * 100.0
    elif transform == "multiply_by_1000":
        value = value * 1000.0

    return round(value, 2)


def fetch_current_period(
    config: dict, start: str, end: str, metrics_requested: list[str]
) -> dict:
    """Fetch metrics for the current period."""
    method, url, headers, auth, body = build_request(config, start, end)

    try:
        if method == "GET":
            resp = requests.get(url, headers=headers, auth=auth, timeout=30)
        else:
            resp = requests.post(url, headers=headers, auth=auth, json=body, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "status_code": getattr(e.response, "status_code", None) if hasattr(e, "response") else None}
    except json.JSONDecodeError:
        return {"error": "Response is not valid JSON", "raw": resp.text[:500]}

    return {"data": data}


def fetch_data(config: dict, start: str, end: str, prev_start: str, prev_end: str) -> dict:
    """Fetch current and previous period data."""
    field_mapping = config.get("field_mapping", {})

    # Current period
    current_result = fetch_current_period(config, start, end, list(field_mapping.keys()))
    if "error" in current_result:
        return {
            "status": "failed",
            "source": "http-api",
            "source_detail": config.get("name", "HTTP API"),
            "period": {"start": start, "end": end},
            "fetched_at": datetime.now().isoformat(),
            "metrics": {},
            "anomalies": [],
            "warnings": [f"API call failed: {current_result['error']}"]
        }

    # Previous period
    prev_config = config.get("previous_period", {})
    prev_strategy = prev_config.get("strategy", "second_api_call")

    if prev_strategy == "second_api_call":
        prev_result = fetch_current_period(config, prev_start, prev_end, list(field_mapping.keys()))
    else:
        prev_result = current_result  # single response contains both

    # Extract and map values
    metrics = {}
    warnings = []

    for metric_key, mapping in field_mapping.items():
        jsonpath = mapping.get("jsonpath", "")

        current_raw = extract_value(current_result.get("data", {}), jsonpath)
        current_val = transform_value(current_raw, mapping)

        if "error" not in prev_result:
            prev_raw = extract_value(prev_result.get("data", {}), jsonpath)
            prev_val = transform_value(prev_raw, mapping)
        else:
            prev_val = None

        if current_val is not None:
            change_pct = None
            if prev_val and prev_val != 0:
                change_pct = round((current_val - prev_val) / prev_val * 100, 1)

            metrics[metric_key] = {
                "value": current_val,
                "previous_value": prev_val,
                "change_pct": change_pct,
                "unit": mapping.get("unit", "number"),
                "status": "ok"
            }
        else:
            metrics[metric_key] = {
                "value": None,
                "previous_value": None,
                "change_pct": None,
                "unit": mapping.get("unit", "number"),
                "status": "not_available",
                "note": f"jsonpath '{jsonpath}' returned null or not found"
            }
            warnings.append(f"{metric_key}: field not found at '{jsonpath}'")

    # Detect anomalies
    anomalies = []
    for key, m in metrics.items():
        if m.get("change_pct") is not None and abs(m["change_pct"]) > 10:
            direction = "上升" if m["change_pct"] > 0 else "下降"
            anomalies.append({
                "metric": key,
                "severity": "critical" if abs(m["change_pct"]) > 20 else "warning",
                "note": f"较上期{direction} {abs(m['change_pct'])}%"
            })

    status = "ok"
    if any(m["status"] == "not_available" for m in metrics.values()):
        status = "partial"
    if all(m["status"] == "not_available" for m in metrics.values()):
        status = "failed"

    return {
        "status": status,
        "source": "http-api",
        "source_detail": config.get("name", "HTTP API"),
        "period": {"start": start, "end": end},
        "fetched_at": datetime.now().isoformat(),
        "metrics": metrics,
        "anomalies": anomalies,
        "warnings": warnings
    }


def main():
    parser = argparse.ArgumentParser(description="HTTP API Data Connector for product-ops")
    parser.add_argument("--config", required=True, help="Path to connector config JSON")
    parser.add_argument("--workflow", required=True, help="Workflow name (weekly-report, daily-brief, etc.)")
    parser.add_argument("--start", required=True, help="Period start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="Period end date (YYYY-MM-DD)")
    parser.add_argument("--prev-start", help="Previous period start date (default: auto-calculate)")
    parser.add_argument("--prev-end", help="Previous period end date (default: auto-calculate)")

    args = parser.parse_args()

    try:
        config = load_config(args.config)
    except FileNotFoundError as e:
        print(json.dumps({
            "status": "failed",
            "source": "http-api",
            "source_detail": "config not found",
            "period": {"start": args.start, "end": args.end},
            "fetched_at": datetime.now().isoformat(),
            "metrics": {},
            "anomalies": [],
            "warnings": [str(e)]
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Calculate previous period
    from datetime import timedelta
    end_dt = datetime.strptime(args.end, "%Y-%m-%d")
    start_dt = datetime.strptime(args.start, "%Y-%m-%d")
    period_days = (end_dt - start_dt).days or 7

    prev_end = args.prev_end or (start_dt - timedelta(days=1)).strftime("%Y-%m-%d")
    prev_start = args.prev_start or (start_dt - timedelta(days=period_days + 1)).strftime("%Y-%m-%d")

    result = fetch_data(config, args.start, args.end, prev_start, prev_end)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
