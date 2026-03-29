# Project Statements – Steam Game Recommender System

---

## Problem Statement

With thousands of games available on platforms like Steam, users often struggle to find games that match their interests. There is a need for a system that can **recommend relevant games efficiently** based on user preferences.

---

## Proposed Solution

Develop a **hybrid game recommender system** that suggests games based on:

* User-selected **genres**
* Games the user already likes
* Game **popularity and ratings**

The system combines multiple techniques to improve accuracy and user experience.

---

## System Approach

The project follows a **hybrid recommendation approach**:

* **Content-Based Filtering** → Uses tags and genres
* **Popularity-Based Ranking** → Uses reviews and ownership data
* **Similarity Matching** → Uses Jaccard similarity between games
* **Diversity Logic** → Prevents repetition and adds randomness

---

## Key Functional Statements

* The system accepts **multiple genres** as input
* The system can recommend games **similar to a given game**
* Each game is assigned a **popularity score**
* Recommendations are selected from a **top-ranked pool**
* Previously recommended games are **not repeated**
* The system provides **dynamic results on each run**

---

## Algorithm Statement

1. Load dataset containing game details
2. Extract relevant fields (name, tags, reviews, owners)
3. Detect genres using keyword matching
4. Accept user input (genre or game name)
5. Apply filtering and scoring logic
6. Rank games based on combined score
7. Select results with diversity mechanism
8. Display recommendations

---

## Data Handling Statement

* Dataset is stored in **CSV format**
* Tags are processed as text for matching
* Numerical fields are used for scoring
* Data is cleaned and normalized before processing

---

## Output Statement

The system outputs:

* A list of **recommended games**
* Based on selected **genres or similar game**
* With **varied and non-repetitive results**

---

## Limitation Statement

* Does not use advanced Machine Learning models
* Depends on dataset quality
* Keyword matching may not capture all genres accurately

---

## Future Enhancement Statement

* Integration of **Machine Learning models (TF-IDF, Cosine Similarity)**
* Development of **GUI or Web Application**
* Use of **real-time APIs (Steam API)**
* Implementation of **user personalization**

---

## Conclusion Statement

The project successfully demonstrates a **hybrid recommender system** that improves game discovery using multiple techniques. It provides a strong base for developing advanced AI-driven recommendation systems.

---
