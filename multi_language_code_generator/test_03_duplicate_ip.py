from log_analyzer import LogAnalyzer


def test_duplicate_ip_addresses():
    lines = [
        "2026-11-12 11:00:00 INFO 10.0.0.1 User logged in",
        "2026-11-12 11:01:00 ERROR 10.0.0.1 Request failed",
        "2026-11-12 11:02:00 INFO 10.0.0.1 User logged out",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 3
    assert result["unique_ips"] == 1
    assert result["error_count"] == 1
    assert result["error_rate"] == 33.33
