#!/usr/bin/python3
"""
A log_parsing module.
"""

import sys


def print_stats(total_size, status_counts):
    """
    Prints the metrics: total file size and status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def log_parsing():
    """
    Reads stdin line by line, parses logs, and computes metrics.
    """
    total_size = 0
    status_counts = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip invalid lines

            # Extract status code and file size
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue  # Skip lines with invalid status code or file size

            # Accumulate total file size
            total_size += file_size

            # Count valid status codes
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Every 10 lines, print the current stats
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # On keyboard interrupt, print the final stats
        print_stats(total_size, status_counts)
        raise

    # Print final stats after reading all lines
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    log_parsing()
