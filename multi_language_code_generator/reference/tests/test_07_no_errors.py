from log_analyzer import LogAnalyzer


def test_no_error_entries():
    lines = [
        "2026-11-12 14:00:00 INFO 192.168.10.1 Request completed",
        "2026-11-12 14:01:00 WARNING 192.168.10.2 High memory usage",
        "2026-11-12 14:02:00 INFO 192.168.10.3 User logged in",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 3
    assert result["error_count"] == 0
    assert result["error_rate"] == 0.0
