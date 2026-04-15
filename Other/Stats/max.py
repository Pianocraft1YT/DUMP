#!/usr/bin/env python3
"""
Read lines of "<stat_key> <player> <value>" from stdin or a file.
For each stat key, find the maximum value. Then count, per player,
how many stats they achieve that maximum (ties count for all tied players).

Handles UTF-8 and UTF-16 encoded files automatically.
"""

import sys
from collections import defaultdict
from pathlib import Path

def read_file_with_encoding_detection(path):
    """
    Attempt to read the file using UTF-8, then UTF-16, then system default.
    Returns the file content as a string.
    """
    encodings = ['utf-8', 'utf-16', sys.getdefaultencoding()]
    for enc in encodings:
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    # If all fail, raise an error
    raise UnicodeDecodeError(f"Could not decode {path} with any of {encodings}")

def main():
    # Read input from file if given, otherwise from stdin
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        data = read_file_with_encoding_detection(input_path)
        lines = data.splitlines()
    else:
        # For stdin, we can't easily detect encoding; assume UTF-8 (common for pipes)
        lines = sys.stdin.read().splitlines()

    # Store stats: dict[stat_key] -> list of (player, value)
    stats = defaultdict(list)

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 3:
            print(f"Skipping malformed line {line_num}: {line}", file=sys.stderr)
            continue
        # The first part is the stat key (may contain colons but no spaces)
        # The second part is the player name (UUID or username, no spaces assumed)
        # The rest is the value
        stat_key = parts[0]
        player = parts[1]
        try:
            value = int(parts[2])
        except ValueError:
            print(f"Invalid value on line {line_num}: {parts[2]}", file=sys.stderr)
            continue
        stats[stat_key].append((player, value))

    # For each stat, find max value
    max_per_stat = {}
    for stat_key, entries in stats.items():
        max_val = max(v for _, v in entries)
        max_per_stat[stat_key] = max_val

    # Count how many times each player reaches the max for a stat
    player_max_count = defaultdict(int)

    for stat_key, entries in stats.items():
        max_val = max_per_stat[stat_key]
        for player, value in entries:
            if value == max_val:
                player_max_count[player] += 1

    # Output results
    print("Player max-stat counts (ties included):")
    for player, count in sorted(player_max_count.items(), key=lambda x: (-x[1], x[0])):
        print(f"{player}: {count}")

if __name__ == "__main__":
    main()