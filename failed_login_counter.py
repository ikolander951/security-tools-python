# Simple script to count failed login attempts in a log file
# Usage: python failed_login_counter.py auth.log

import sys
from collections import Counter

def count_failed_logins(log_path: str) -> None:
    keywords = ("failed password", "authentication failure")
    counts = Counter()

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            lower = line.lower()
            if any(k in lower for k in keywords):
                counts["failed"] += 1

    total_failed = counts["failed"]
    print(f"Total failed login-related entries: {total_failed}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python failed_login_counter.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    count_failed_logins(log_file)
