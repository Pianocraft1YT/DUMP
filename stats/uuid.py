import json
import sys

def read_json_with_encoding(file_path):
    encodings = ['utf-16', 'utf-8-sig', 'utf-8']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise Exception(f"Could not read {file_path} with any tried encoding.")

def extract_players_from_maxstats(input_file, output_file=None):
    try:
        data = read_json_with_encoding(input_file)
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    if not isinstance(data, dict):
        print("Error: Input JSON is not a dictionary.")
        return

    # Collect all unique player filenames from the "player" field
    players = set()
    for stat_info in data.values():
        if isinstance(stat_info, dict) and 'player' in stat_info:
            players.add(stat_info['player'])

    sorted_players = sorted(players)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for player in sorted_players:
                f.write(player + '\n')
        print(f"Extracted {len(sorted_players)} unique players to {output_file}")
    else:
        for player in sorted_players:
            print(player)
        print(f"Total: {len(sorted_players)} unique players")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_players.py <max_stats.json> [output.txt]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_players_from_maxstats(input_file, output_file)