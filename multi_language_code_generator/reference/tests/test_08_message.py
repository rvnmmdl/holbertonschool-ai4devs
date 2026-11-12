from log_analyzer import LogAnalyzer


def test_message_with_multiple_words():
    line = (
        "2026-11-12 15:00:00 ERROR 192.168.1.20 "
        "Database connection failed unexpectedly"
    )

    entry = LogAnalyzer().parse_line(line)

    assert entry is not None
    assert entry["message"] == "Database connection failed unexpectedly"
