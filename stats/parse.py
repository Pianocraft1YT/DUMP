#!/usr/bin/env python3
"""
Parse a Minecraft stats file in the format shown in the user's message.
Each line of output contains: <stat_key> <player> <value>
"""

import json
import re
import sys
from pathlib import Path

def clean_json(text):
    """
    Remove trailing commas before closing braces/brackets.
    This handles the most common issue in the given format.
    """
    # Remove commas that are followed by optional whitespace and then } or ]
    # We use a regex with a negative lookbehind to avoid removing commas inside strings,
    # but it's simpler to just replace globally; inside strings the pattern is unlikely.
    # However, to be safer, we can use a more robust approach: parse with a tolerant library.
    # Here we'll do a simple replace.
    text = re.sub(r',\s*\}', '}', text)
    text = re.sub(r',\s*\]', ']', text)
    return text

def main():
    # Read input from file if given, otherwise from stdin
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        data_text = input_path.read_text(encoding='utf-8')
    else:
        data_text = sys.stdin.read()

    # Attempt to parse as JSON; if it fails, try cleaning trailing commas.
    try:
        data = json.loads(data_text)
    except json.JSONDecodeError:
        # Try cleaning
        cleaned = clean_json(data_text)
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            print(f"Error: Unable to parse JSON even after cleaning: {e}", file=sys.stderr)
            sys.exit(1)

    # Ensure data is a dictionary
    if not isinstance(data, dict):
        print("Error: Top-level JSON is not an object.", file=sys.stderr)
        sys.exit(1)

    # Iterate over each stat entry
    for stat_key, entry in data.items():
        # Each entry should be a dict with "player" and "value"
        if not isinstance(entry, dict):
            # Skip if not a dict (maybe malformed)
            continue
        player = entry.get("player")
        value = entry.get("value")
        if player is None or value is None:
            # Skip incomplete entries
            continue
        # Output: stat_key, player, value
        print(f"{stat_key} {player} {value}")

if __name__ == "__main__":
    main()