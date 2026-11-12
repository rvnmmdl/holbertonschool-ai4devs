# Cross-Language Specification - Log Analyzer

## 1. Algorithm Description

The Log Analyzer processes application log entries and calculates summary statistics.

For each valid log entry, the algorithm extracts:

- Timestamp
- Log level
- Message
- IP address

The algorithm then calculates:

1. Total number of valid requests/log entries
2. Number of successful entries (`INFO`)
3. Number of warning entries (`WARNING`)
4. Number of error entries (`ERROR`)
5. Number of unique IP addresses
6. Error rate as a percentage

The algorithm must produce the same result regardless of the programming language used to implement it.

---

## 2. Input Format

The input is a collection of log entries.

Each entry must use the following format:

```text
YYYY-MM-DD HH:MM:SS LEVEL IP_ADDRESS MESSAGE
```

Example:

```text
2026-11-12 10:00:00 INFO 192.168.1.10 User logged in
2026-11-12 10:01:00 INFO 192.168.1.11 Page requested
2026-11-12 10:02:00 ERROR 192.168.1.10 Database connection failed
2026-11-12 10:03:00 WARNING 192.168.1.12 Disk usage is high
```

### Supported Log Levels

The following log levels are supported:

- `INFO`
- `WARNING`
- `ERROR`

A valid IP address is required for each valid entry.

The message may contain multiple words.

---

## 3. Output Format

The algorithm must return a JSON-compatible object with the following fields:

```json
{
  "total_entries": 4,
  "info_count": 2,
  "warning_count": 1,
  "error_count": 1,
  "unique_ips": 3,
  "error_rate": 25.0
}
```

### Output Field Definitions

| Field | Description |
|---|---|
| `total_entries` | Number of valid log entries |
| `info_count` | Number of `INFO` entries |
| `warning_count` | Number of `WARNING` entries |
| `error_count` | Number of `ERROR` entries |
| `unique_ips` | Number of unique IP addresses |
| `error_rate` | Percentage of valid entries with `ERROR` level |

The error rate is calculated as:

```text
error_rate = (error_count / total_entries) * 100
```

The result must be rounded to two decimal places.

If there are no valid entries, `error_rate` must be `0.0`.

---

## 4. Processing Rules

The implementation must follow these rules:

1. Process each input line independently.
2. Ignore empty lines.
3. Parse the timestamp, log level, IP address, and message.
4. Count only entries with a supported log level.
5. Add each valid IP address to the set of unique IP addresses.
6. Count `INFO`, `WARNING`, and `ERROR` entries separately.
7. Calculate the error rate using only valid entries.
8. Do not modify the original input data.
9. Preserve the same output structure across programming languages.

---

## 5. Edge Cases

The implementation must correctly handle the following situations:

### Empty Input

Input:

```text
```

Expected behavior:

```json
{
  "total_entries": 0,
  "info_count": 0,
  "warning_count": 0,
  "error_count": 0,
  "unique_ips": 0,
  "error_rate": 0.0
}
```

### Empty Lines

Empty lines should be ignored and must not increase the total entry count.

### Malformed Entries

Example:

```text
This is not a valid log entry
```

Malformed entries should be ignored.

### Unsupported Log Level

Example:

```text
2026-11-12 10:05:00 DEBUG 192.168.1.20 Debug message
```

Since `DEBUG` is not supported, this entry should not be included in the statistics.

### Duplicate IP Addresses

Multiple entries from the same IP address should count as one unique IP.

### Only Error Entries

If all valid entries are `ERROR`, the error rate must be `100.0`.

### No Error Entries

If there are valid entries but none have the `ERROR` level, the error rate must be `0.0`.

### Message With Multiple Words

The message may contain spaces and multiple words. The parser must not incorrectly split the message.

---

# 6. Test Cases

## Test Case 1 - Normal Input

### Input

```text
2026-11-12 10:00:00 INFO 192.168.1.10 User logged in
2026-11-12 10:01:00 INFO 192.168.1.11 Page requested
2026-11-12 10:02:00 ERROR 192.168.1.10 Database connection failed
2026-11-12 10:03:00 WARNING 192.168.1.12 Disk usage is high
```

### Expected Output

```json
{
  "total_entries": 4,
  "info_count": 2,
  "warning_count": 1,
  "error_count": 1,
  "unique_ips": 3,
  "error_rate": 25.0
}
```

---

## Test Case 2 - Empty Input

### Input

```text
```

### Expected Output

```json
{
  "total_entries": 0,
  "info_count": 0,
  "warning_count": 0,
  "error_count": 0,
  "unique_ips": 0,
  "error_rate": 0.0
}
```

---

## Test Case 3 - Duplicate IP Addresses

### Input

```text
2026-11-12 11:00:00 INFO 10.0.0.1 User logged in
2026-11-12 11:01:00 ERROR 10.0.0.1 Request failed
2026-11-12 11:02:00 INFO 10.0.0.1 User logged out
```

### Expected Output

```json
{
  "total_entries": 3,
  "info_count": 2,
  "warning_count": 0,
  "error_count": 1,
  "unique_ips": 1,
  "error_rate": 33.33
}
```

---

## Test Case 4 - Malformed and Unsupported Entries

### Input

```text
2026-11-12 12:00:00 INFO 192.168.1.5 Valid request
This line is malformed
2026-11-12 12:01:00 DEBUG 192.168.1.6 Debug request
2026-11-12 12:02:00 ERROR 192.168.1.7 Server failed
```

### Expected Output

```json
{
  "total_entries": 2,
  "info_count": 1,
  "warning_count": 0,
  "error_count": 1,
  "unique_ips": 2,
  "error_rate": 50.0
}
```

The malformed line and the unsupported `DEBUG` entry must be ignored.

---

## Test Case 5 - Only Error Entries

### Input

```text
2026-11-12 13:00:00 ERROR 172.16.0.1 Database unavailable
2026-11-12 13:01:00 ERROR 172.16.0.2 Server unavailable
```

### Expected Output

```json
{
  "total_entries": 2,
  "info_count": 0,
  "warning_count": 0,
  "error_count": 2,
  "unique_ips": 2,
  "error_rate": 100.0
}
```

---

## Test Case 6 - No Error Entries

### Input

```text
2026-11-12 14:00:00 INFO 192.168.10.1 Request completed
2026-11-12 14:01:00 WARNING 192.168.10.2 High memory usage
2026-11-12 14:02:00 INFO 192.168.10.3 User logged in
```

### Expected Output

```json
{
  "total_entries": 3,
  "info_count": 2,
  "warning_count": 1,
  "error_count": 0,
  "unique_ips": 3,
  "error_rate": 0.0
}
```

---

## 7. Cross-Language Requirements

The implementation may be written in any programming language, but every implementation must follow the same specification.

For example, the algorithm can be implemented in:

- Python
- JavaScript
- Java
- C#
- Go

Different implementations must produce equivalent outputs for the same input.

Language-specific syntax, libraries, and data structures may differ, but the following must remain consistent:

- Input format
- Supported log levels
- Validation rules
- Counting rules
- Unique IP calculation
- Error rate calculation
- Edge-case behavior
- Output field names
- Output value meanings

## 8. Definition of Success

An implementation is considered correct when it:

1. Correctly parses valid log entries.
2. Ignores malformed and unsupported entries.
3. Correctly counts each supported log level.
4. Correctly calculates unique IP addresses.
5. Correctly calculates the error rate.
6. Correctly handles all defined edge cases.
7. Produces the required output structure.
8. Passes all six test cases.