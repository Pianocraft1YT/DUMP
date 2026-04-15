import json
import glob
import os
from collections import defaultdict

# Dictionary to store the maximum for each statistic
# Key: full statistic path (e.g., "minecraft:mined:minecraft:stone")
# Value: tuple (max_value, player_filename)
max_stats = {}

# Process each JSON file
for filename in glob.glob("*.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        continue

    stats = data.get("stats", {})
    # Iterate over each category (mined, custom, killed, etc.)
    for category, contents in stats.items():
        if not isinstance(contents, dict):
            continue
        for stat_name, value in contents.items():
            if not isinstance(value, (int, float)):
                continue
            full_key = f"{category}:{stat_name}"
            if full_key not in max_stats or value > max_stats[full_key][0]:
                max_stats[full_key] = (value, filename)

# Output the results sorted by key
print(json.dumps({k: {"player": v[1], "value": v[0]} for k, v in sorted(max_stats.items())}, indent=2))