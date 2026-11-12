import unittest

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_normal_input(self):
        lines = [
            "2026-11-12 10:00:00 INFO 192.168.1.10 User logged in",
            "2026-11-12 10:01:00 INFO 192.168.1.11 Page requested",
            "2026-11-12 10:02:00 ERROR 192.168.1.10 Database connection failed",
            "2026-11-12 10:03:00 WARNING 192.168.1.12 Disk usage is high",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 4)
        self.assertEqual(result["info_count"], 2)
        self.assertEqual(result["warning_count"], 1)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["unique_ips"], 3)
        self.assertEqual(result["error_rate"], 25.0)

    def test_empty_input(self):
        result = self.analyzer.analyze([])

        self.assertEqual(
            result,
            {
                "total_entries": 0,
                "info_count": 0,
                "warning_count": 0,
                "error_count": 0,
                "unique_ips": 0,
                "error_rate": 0.0,
            },
        )

    def test_duplicate_ip_addresses(self):
        lines = [
            "2026-11-12 11:00:00 INFO 10.0.0.1 User logged in",
            "2026-11-12 11:01:00 ERROR 10.0.0.1 Request failed",
            "2026-11-12 11:02:00 INFO 10.0.0.1 User logged out",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 3)
        self.assertEqual(result["unique_ips"], 1)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["error_rate"], 33.33)

    def test_malformed_entries_are_ignored(self):
        lines = [
            "2026-11-12 12:00:00 INFO 192.168.1.5 Valid request",
            "This line is malformed",
            "2026-11-12 12:02:00 ERROR 192.168.1.7 Server failed",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["unique_ips"], 2)

    def test_unsupported_log_level_is_ignored(self):
        lines = [
            "2026-11-12 12:00:00 INFO 192.168.1.5 Valid request",
            "2026-11-12 12:01:00 DEBUG 192.168.1.6 Debug request",
            "2026-11-12 12:02:00 ERROR 192.168.1.7 Server failed",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["info_count"], 1)
        self.assertEqual(result["error_count"], 1)

    def test_only_error_entries(self):
        lines = [
            "2026-11-12 13:00:00 ERROR 172.16.0.1 Database unavailable",
            "2026-11-12 13:01:00 ERROR 172.16.0.2 Server unavailable",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["error_count"], 2)
        self.assertEqual(result["error_rate"], 100.0)

    def test_no_error_entries(self):
        lines = [
            "2026-11-12 14:00:00 INFO 192.168.10.1 Request completed",
            "2026-11-12 14:01:00 WARNING 192.168.10.2 High memory usage",
            "2026-11-12 14:02:00 INFO 192.168.10.3 User logged in",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 3)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    def test_message_with_multiple_words(self):
        line = (
            "2026-11-12 15:00:00 ERROR 192.168.1.20 "
            "Database connection failed unexpectedly"
        )

        entry = self.analyzer.parse_line(line)

        self.assertIsNotNone(entry)
        self.assertEqual(
            entry["message"],
            "Database connection failed unexpectedly",
        )

    def test_empty_lines_are_ignored(self):
        lines = [
            "",
            "   ",
            "2026-11-12 16:00:00 INFO 192.168.1.1 Valid request",
            "",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 1)
        self.assertEqual(result["info_count"], 1)

    def test_invalid_ip_is_ignored(self):
        lines = [
            "2026-11-12 17:00:00 INFO 192.168.1.1 Valid request",
            "2026-11-12 17:01:00 ERROR 999.999.999.999 Invalid IP",
            "2026-11-12 17:02:00 WARNING 10.0.0.1 Valid warning",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["unique_ips"], 2)
        self.assertEqual(result["error_count"], 0)

    def test_ip_address_with_zero_octet(self):
        lines = [
            "2026-11-12 18:00:00 INFO 0.0.0.0 Valid request",
            "2026-11-12 18:01:00 ERROR 255.255.255.255 Server failed",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["unique_ips"], 2)
        self.assertEqual(result["error_rate"], 50.0)

    def test_mixed_valid_invalid_and_duplicate_entries(self):
        lines = [
            "2026-11-12 19:00:00 INFO 10.0.0.1 Login successful",
            "2026-11-12 19:01:00 ERROR 10.0.0.2 Database failed",
            "invalid log entry",
            "2026-11-12 19:02:00 WARNING 10.0.0.1 High memory usage",
            "2026-11-12 19:03:00 DEBUG 10.0.0.3 Debug message",
            "2026-11-12 19:04:00 ERROR 10.0.0.2 Another database failure",
        ]

        result = self.analyzer.analyze(lines)

        self.assertEqual(result["total_entries"], 4)
        self.assertEqual(result["info_count"], 1)
        self.assertEqual(result["warning_count"], 1)
        self.assertEqual(result["error_count"], 2)
        self.assertEqual(result["unique_ips"], 2)
        self.assertEqual(result["error_rate"], 50.0)


if __name__ == "__main__":
    unittest.main()