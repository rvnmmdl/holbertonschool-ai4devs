from log_analyzer import LogAnalyzer


def test_empty_lines_are_ignored():
    lines = [
        "",
        "   ",
        "2026-11-12 16:00:00 INFO 192.168.1.1 Valid request",
        "",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 1
    assert result["info_count"] == 1
