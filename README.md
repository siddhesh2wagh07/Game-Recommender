# Steam Game Recommender System

<p align="center">
  <b>A hybrid recommendation system built with Python</b><br>
  Genre-Based • Similarity-Based • Popularity Ranking
</p>

---

## Overview

This project is a **hybrid game recommender system** that suggests games based on:

*  User-selected **genres**
*  Games the user already likes
*  Game **popularity and ratings**

It combines multiple techniques to provide **smart, diverse, and non-repetitive recommendations**.

---

##  Features

*  Multi-genre input (e.g., `action, open_world`)
*  “Games like X” recommendation
*  Popularity-based ranking system
*  Non-repetitive suggestions (session memory)
*  Dynamic results (randomized top picks)
*  Clean CLI-based user interface

---

## How It Works

### 1. Genre-Based Filtering

* Matches game tags with predefined genre keywords
* Supports multiple genres
* More matching genres = higher score

### 2. Popularity Ranking

Games are ranked using:

```python
score = positive - negative + (owners // 1000)
```

---

### 3. Similarity Recommendation

* Uses **Jaccard Similarity**
* Compares tags between games
* Finds games most similar to the input game

---

### 4. Smart Diversity System

* Selects from **top 50 results**
* Uses randomness to keep recommendations fresh
* Avoids repeating already shown games

---

## Tech Stack

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Core programming             |
| csv        | Dataset handling             |
| random     | Diversity in recommendations |

---

## Dataset

**File:** `steam_games_large.csv`

### Required Columns:

* `name`
* `tags`
* `positive`
* `negative`
* `owners`

>  Make sure the dataset is in the same folder as `main.py`

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/steam-recommender.git
cd steam-recommender
```

### Add Dataset

Place the dataset file:

```
steam_games_large.csv
```

### Run the Project

```bash
python main.py
```

---

## Usage

```
1️. Recommend by Genre
2️. Recommend Games Like X
3️. Exit
```

### Example:

**Input:**

```
action, open_world
```

**Output:**

```
GTA V
Red Dead Redemption 2
Cyberpunk 2077
...

```
---

## Limitations

* No advanced ML 
* Depends on dataset quality
* Keyword-based genre detection

---

## Conclusion

This project demonstrates a **real-world recommender system approach** using:

* Hybrid filtering
* Ranking strategies
* Diversity handling

It serves as a strong foundation for building advanced AI-based recommendation systems.

---
