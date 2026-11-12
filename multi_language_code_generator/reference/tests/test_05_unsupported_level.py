from log_analyzer import LogAnalyzer


def test_unsupported_log_level_is_ignored():
    lines = [
        "2026-11-12 12:00:00 INFO 192.168.1.5 Valid request",
        "2026-11-12 12:01:00 DEBUG 192.168.1.6 Debug request",
        "2026-11-12 12:02:00 ERROR 192.168.1.7 Server failed",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 2
    assert result["info_count"] == 1
    assert result["error_count"] == 1
