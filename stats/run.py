import json
import sys
from collections import OrderedDict

def read_json_with_encoding(file_path):
    """Try to read JSON file with multiple encodings."""
    encodings = ['utf-8-sig', 'utf-16', 'utf-8']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise Exception(f"Could not read {file_path} with any tried encoding.")

def sort_max_stats_by_player(input_file, output_file):
    try:
        data = read_json_with_encoding(input_file)
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    if not isinstance(data, dict):
        print("Error: Input JSON is not a dictionary.")
        return

    # Convert to list of (stat_key, player, value) for sorting
    entries = [(stat, info['player'], info['value']) for stat, info in data.items()]

    # Sort by player (UUID), then by statistic key for consistency
    entries.sort(key=lambda x: (x[1], x[0]))

    # Rebuild ordered dictionary
    sorted_data = OrderedDict()
    for stat, player, value in entries:
        sorted_data[stat] = {"player": player, "value": value}

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, indent=2)
        print(f"Sorted max stats written to {output_file}")
    except Exception as e:
        print(f"Error writing {output_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sort_max_by_player.py <input_max.json> <output_max.json>")
    else:
        sort_max_stats_by_player(sys.argv[1], sys.argv[2])