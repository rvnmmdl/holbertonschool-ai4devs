import json
from datetime import datetime

def load_config(raw):
    return json.loads(raw)


def total_price(prices):
    return sum(float(p) for p in prices)


def is_adult(age_text):
    return int(age_text) > 18


def parse_deadline(text):
    return datetime.strptime(text, "%Y-%m-%d")


def check(label, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"{label} | expected={expected} | actual={actual} | {status}")
    assert expected == actual


if __name__ == "__main__":
    cfg = load_config(json.dumps({"currency": "AZN", "tax": 0.18}))
    check("load_config currency", "AZN", cfg["currency"])
    check("load_config tax", 0.18, cfg["tax"])
    check("total_price(['10.5','20','5.25'])", 35.75, total_price(["10.5", "20", "5.25"]))
    check("total_price([])", 0, total_price([]))
    check("is_adult('25')", True, is_adult("25"))
    check("is_adult('10')", False, is_adult("10"))
    check("parse_deadline('2026-11-09')", datetime(2026, 11, 9), parse_deadline("2026-11-09"))
    try:
        parse_deadline("09/11/2026")
        check("wrong date format raises ValueError", True, False)
    except ValueError:
        check("wrong date format raises ValueError", True, True)
