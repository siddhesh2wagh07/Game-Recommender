# 🎮 Steam Game Recommender System

<p align="center">
  <b>A hybrid recommendation system built with Python</b><br>
  Genre-Based • Similarity-Based • Popularity Ranking
</p>

---

## 🚀 Overview

This project is a **hybrid game recommender system** that suggests games based on:

* 🎯 User-selected **genres**
* 🎮 Games the user already likes
* 🔥 Game **popularity and ratings**

It combines multiple techniques to provide **smart, diverse, and non-repetitive recommendations**.

---

## ✨ Features

* ✅ Multi-genre input (e.g., `action, open_world`)
* ✅ “Games like X” recommendation
* ✅ Popularity-based ranking system
* ✅ Non-repetitive suggestions (session memory)
* ✅ Dynamic results (randomized top picks)
* ✅ Clean CLI-based user interface

---

## 🧠 How It Works

### 🔹 1. Genre-Based Filtering

* Matches game tags with predefined genre keywords
* Supports multiple genres
* More matching genres = higher score

### 🔹 2. Popularity Ranking

Games are ranked using:

```python
score = positive - negative + (owners // 1000)
```

---

### 🔹 3. Similarity Recommendation

* Uses **Jaccard Similarity**
* Compares tags between games
* Finds games most similar to the input game

---

### 🔹 4. Smart Diversity System

* Selects from **top 50 results**
* Uses randomness to keep recommendations fresh
* Avoids repeating already shown games

---

## 🛠️ Tech Stack

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Core programming             |
| csv        | Dataset handling             |
| random     | Diversity in recommendations |

---

## 📂 Dataset

**File:** `steam_games_large.csv`

### Required Columns:

* `name`
* `tags`
* `positive`
* `negative`
* `owners`

> ⚠️ Make sure the dataset is in the same folder as `main.py`

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/steam-recommender.git
cd steam-recommender
```

### 2️⃣ Add Dataset

Place the dataset file:

```
steam_games_large.csv
```

### 3️⃣ Run the Project

```bash
import csv
import random

# 🎯 Define genres
GENRES = {
    "fps": ["fps", "shooter", "gun", "first person"],
    "horror": ["horror", "scary", "fear", "evil", "ghost"],
    "rpg": ["rpg", "role", "fantasy", "souls"],
    "open_world": ["open", "world", "sandbox"],
    "survival": ["survival", "craft", "zombie"],
    "multiplayer": ["multiplayer", "online", "co-op"],
    "racing": ["racing", "cars", "driving"],
    "sports": ["sports", "football", "basketball"],
    "strategy": ["strategy", "rts", "tactics"],
    "simulation": ["simulation", "simulator"],
    "adventure": ["adventure", "story"],
    "action": ["action", "combat", "fight"],
    "stealth": ["stealth", "sneak", "assassin"]
}

games = []
seen_games = set()  # 🔥 Prevent repetition

# 🎯 Popularity score
def get_popularity_score(row):
    try:
        positive = int(row.get("positive", 0))
        negative = int(row.get("negative", 0))
        owners = row.get("owners", "0")

        if "-" in owners:
            owners = int(owners.split("-")[0])
        else:
            owners = int(owners)

        return positive - negative + (owners // 1000)
    except:
        return 0


# 🎯 Load dataset
with open("steam_games_large.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        tags = row["tags"].lower()

        if name and tags:
            games.append({
                "name": name,
                "tags": tags,
                "score": get_popularity_score(row)
            })

print(f"✅ Loaded {len(games)} games\n")


# 🎯 Detect genres
def detect_game_genres(game):
    detected = []

    for genre, keywords in GENRES.items():
        for word in keywords:
            if word in game["tags"]:
                detected.append(genre)
                break

    return detected


# 🎯 Genre-based recommender (NO REPEAT + VARIETY)
def recommend_by_genres(user_genres, top_n=7):
    results = []

    for game in games:
        detected = detect_game_genres(game)
        match_count = len(set(user_genres) & set(detected))

        if match_count > 0:
            final_score = (match_count * 10) + game["score"]
            results.append((final_score, game))

    results.sort(key=lambda x: x[0], reverse=True)

    # 🎯 Top pool for variety
    top_pool = [game for _, game in results[:50]]

    # Remove seen games
    filtered = [g for g in top_pool if g["name"] not in seen_games]

    if len(filtered) < top_n:
        seen_games.clear()
        filtered = top_pool

    selected = random.sample(filtered, min(top_n, len(filtered)))

    for g in selected:
        seen_games.add(g["name"])

    return selected


# 🎯 Similar games recommender (NO REPEAT + VARIETY)
def recommend_similar_games(game_name, top_n=7):
    target_game = None

    for game in games:
        if game_name.lower() in game["name"].lower():
            target_game = game
            break

    if not target_game:
        return []

    target_tags = set(target_game["tags"].split(","))
    similarities = []

    for game in games:
        if game == target_game:
            continue

        game_tags = set(game["tags"].split(","))

        intersection = len(target_tags & game_tags)
        union = len(target_tags | game_tags)

        if union == 0:
            continue

        similarity_score = intersection / union
        final_score = (similarity_score * 100) + (game["score"] / 1000)

        similarities.append((final_score, game))

    similarities.sort(key=lambda x: x[0], reverse=True)

    # 🎯 Top pool
    top_pool = [game for _, game in similarities[:50]]

    filtered = [g for g in top_pool if g["name"] not in seen_games]

    if len(filtered) < top_n:
        seen_games.clear()
        filtered = top_pool

    selected = random.sample(filtered, min(top_n, len(filtered)))

    for g in selected:
        seen_games.add(g["name"])

    return selected


# 🎮 MAIN UI
def main():
    print("🎮 ADVANCED Steam Recommender System\n")

    while True:
        print("\nChoose what you want to do:\n")
        print("1️⃣ Recommend by Genre")
        print("2️⃣ Recommend Games Like X")
        print("3️⃣ Exit")

        choice = input("\n👉 Enter choice (1/2/3): ").strip()

        # 🎯 GENRE
        if choice == "1":
            print("\nAvailable genres:\n")
            for g in GENRES:
                print(f"👉 {g}")

            user_input = input("\n👉 Enter genres (comma-separated): ").lower()
            user_genres = [g.strip() for g in user_input.split(",")]

            valid_genres = [g for g in user_genres if g in GENRES]

            if not valid_genres:
                print("❌ No valid genres entered")
                continue

            results = recommend_by_genres(valid_genres)

            if not results:
                print("❌ No games found")
                continue

            print("\n🔥 Recommended Games:\n")
            for game in results:
                print(f"🎯 {game['name']}")

            print("\n" + "-"*40)

        # 🎯 SIMILAR
        elif choice == "2":
            game_name = input("\n🎮 Enter a game you like: ")

            results = recommend_similar_games(game_name)

            if not results:
                print("❌ Game not found or no similar games")
                continue

            print("\n🔥 Similar Games:\n")
            for game in results:
                print(f"🎯 {game['name']}")

            print("\n" + "-"*40)

        # 🎯 EXIT
        elif choice == "3":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
```

---

## 💻 Usage

```
1️⃣ Recommend by Genre
2️⃣ Recommend Games Like X
3️⃣ Exit
```

### Example:

**Input:**

```
action, open_world
```

**Output:**

```
🎯 GTA V
🎯 Red Dead Redemption 2
🎯 Cyberpunk 2077
...

```
---

## ⚠️ Limitations

* No advanced ML (yet)
* Depends on dataset quality
* Keyword-based genre detection

---

## 🏁 Conclusion

This project demonstrates a **real-world recommender system approach** using:

* Hybrid filtering
* Ranking strategies
* Diversity handling

It serves as a strong foundation for building advanced AI-based recommendation systems.

---
