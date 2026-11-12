from log_analyzer import LogAnalyzer


def test_malformed_entries_are_ignored():
    lines = [
        "2026-11-12 12:00:00 INFO 192.168.1.5 Valid request",
        "This line is malformed",
        "2026-11-12 12:02:00 ERROR 192.168.1.7 Server failed",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 2
    assert result["error_count"] == 1
    assert result["unique_ips"] == 2
