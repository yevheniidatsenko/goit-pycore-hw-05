import sys
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """
    Parse a log line into a dictionary with date, time, level, and message.
    """
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)"
    match = re.match(pattern, line)
    if match:
        return {
            "date": match.group(1),
            "time": match.group(2),
            "level": match.group(3),
            "message": match.group(4)
        }
    else:
        raise ValueError("Invalid log line format")

def load_logs(file_path: str) -> list:
    """
    Load logs from a file and parse each line into a dictionary.
    """
    try:
        with open(file_path, "r") as file:
            logs = [parse_log_line(line.strip()) for line in file]
            return logs
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs by a specific level.
    """
    return [log for log in logs if log["level"] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """
    Count logs by level.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)

def display_log_counts(counts: dict) -> None:
    """
    Display log counts in a table format.
    """
    print("Level | Count")
    print("-----|-----")
    for level, count in counts.items():
        print(f"{level:<7} | {count}")

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nDetails for level '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()