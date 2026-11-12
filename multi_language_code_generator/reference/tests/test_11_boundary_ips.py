from log_analyzer import LogAnalyzer


def test_boundary_ipv4_addresses():
    lines = [
        "2026-11-12 18:00:00 INFO 0.0.0.0 Valid request",
        "2026-11-12 18:01:00 ERROR 255.255.255.255 Server failed",
    ]

    result = LogAnalyzer().analyze(lines)

    assert result["total_entries"] == 2
    assert result["unique_ips"] == 2
    assert result["error_rate"] == 50.0
