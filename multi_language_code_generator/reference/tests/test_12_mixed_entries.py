from log_analyzer import LogAnalyzer


def test_mixed_valid_invalid_and_duplicate_entries():
    lines = [
        "2026-11-12 19:00:00 INFO 10.0.0.1 Login successful",
        "2026-11-12 19:01:00 ERROR 10.0.0.2 Database failed",
        "invalid log entry",
        "2026-11-12 19:02:00 WARNING 10.0.0.1 High memory usage",
        "2026-11-12 19:03:00 DEBUG 10.0.0.3 Debug message",
        "2026-11-12 19:04:00 ERROR 10.0.0.2 Another database failure",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 4
    assert result["info_count"] == 1
    assert result["warning_count"] == 1
    assert result["error_count"] == 2
    assert result["unique_ips"] == 2
    assert result["error_rate"] == 50.0
