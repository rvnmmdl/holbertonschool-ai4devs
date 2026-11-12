from log_analyzer import LogAnalyzer


def test_empty_input():
    assert LogAnalyzer().analyze([]) == {
        "total_entries": 0,
        "info_count": 0,
        "warning_count": 0,
        "error_count": 0,
        "unique_ips": 0,
        "error_rate": 0.0,
    }
