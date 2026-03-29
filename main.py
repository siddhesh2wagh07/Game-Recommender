import requests
import csv
import time

output_file = "steam_games_large.csv"

print("📥 Downloading LARGE Steam dataset...")

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "tags"])

    total_saved = 0

    for page in range(0, 50):
        print(f"Fetching page {page}...")

        url = f"https://steamspy.com/api.php?request=all&page={page}"
        response = requests.get(url)
        data = response.json()

        if not data:
            print("No more data, stopping...")
            break

        for appid, game in data.items():
            name = game.get("name", "")

            # 🔥 FIX: use tags OR genre OR fallback
            tags = game.get("tags", "")
            genre = game.get("genre", "")

            combined = f"{tags} {genre}".strip()

            if not combined:
                combined = name  # last fallback

            writer.writerow([name, combined])
            total_saved += 1

        time.sleep(1)

print(f"✅ Done! Saved {total_saved} games to {output_file}")