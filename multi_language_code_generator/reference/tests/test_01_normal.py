from log_analyzer import LogAnalyzer


def test_normal_input():
    lines = [
        "2026-11-12 10:00:00 INFO 192.168.1.10 User logged in",
        "2026-11-12 10:01:00 INFO 192.168.1.11 Page requested",
        "2026-11-12 10:02:00 ERROR 192.168.1.10 Database connection failed",
        "2026-11-12 10:03:00 WARNING 192.168.1.12 Disk usage is high",
    ]

    assert LogAnalyzer().analyze(lines) == {
        "total_entries": 4,
        "info_count": 2,
        "warning_count": 1,
        "error_count": 1,
        "unique_ips": 3,
        "error_rate": 25.0,
    }
