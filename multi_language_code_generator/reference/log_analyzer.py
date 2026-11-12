from typing import Iterable


class LogAnalyzer:
    """Analyze application log entries."""

    SUPPORTED_LEVELS = {"INFO", "WARNING", "ERROR"}

    def parse_line(self, line: str) -> dict | None:
        if not line or not line.strip():
            return None

        parts = line.strip().split(maxsplit=4)

        if len(parts) < 5:
            return None

        timestamp_date, timestamp_time, level, ip_address, message = parts

        if level not in self.SUPPORTED_LEVELS:
            return None

        if not self._is_valid_ip(ip_address):
            return None

        return {
            "timestamp": f"{timestamp_date} {timestamp_time}",
            "level": level,
            "ip": ip_address,
            "message": message,
        }

    def analyze(self, lines: Iterable[str]) -> dict:
        total_entries = 0
        info_count = 0
        warning_count = 0
        error_count = 0
        unique_ips = set()

        for line in lines:
            entry = self.parse_line(line)

            if entry is None:
                continue

            total_entries += 1
            unique_ips.add(entry["ip"])

            if entry["level"] == "INFO":
                info_count += 1
            elif entry["level"] == "WARNING":
                warning_count += 1
            elif entry["level"] == "ERROR":
                error_count += 1

        error_rate = (
            round((error_count / total_entries) * 100, 2)
            if total_entries > 0
            else 0.0
        )

        return {
            "total_entries": total_entries,
            "info_count": info_count,
            "warning_count": warning_count,
            "error_count": error_count,
            "unique_ips": len(unique_ips),
            "error_rate": error_rate,
        }

    @staticmethod
    def _is_valid_ip(ip_address: str) -> bool:
        parts = ip_address.split(".")

        if len(parts) != 4:
            return False

        try:
            octets = [int(part) for part in parts]
        except ValueError:
            return False

        return all(0 <= octet <= 255 for octet in octets)
