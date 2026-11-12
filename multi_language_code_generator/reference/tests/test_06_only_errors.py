from log_analyzer import LogAnalyzer


def test_only_error_entries():
    lines = [
        "2026-11-12 13:00:00 ERROR 172.16.0.1 Database unavailable",
        "2026-11-12 13:01:00 ERROR 172.16.0.2 Server unavailable",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 2
    assert result["error_count"] == 2
    assert result["error_rate"] == 100.0
