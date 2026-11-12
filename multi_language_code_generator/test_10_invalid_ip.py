from log_analyzer import LogAnalyzer


def test_invalid_ip_is_ignored():
    lines = [
        "2026-11-12 17:00:00 INFO 192.168.1.1 Valid request",
        "2026-11-12 17:01:00 ERROR 999.999.999.999 Invalid IP",
        "2026-11-12 17:02:00 WARNING 10.0.0.1 Valid warning",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 2
    assert result["unique_ips"] == 2
    assert result["error_count"] == 0
