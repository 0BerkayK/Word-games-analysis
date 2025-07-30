import pandas as pd
import random

# 30 target words (Easy, Medium, Hard)
words = [
    # Easy
    ("CAT", "Easy"), ("SUN", "Easy"), ("MOON", "Easy"), ("DOG", "Easy"),
    ("TREE", "Easy"), ("LAMP", "Easy"), ("BOOK", "Easy"), ("STAR", "Easy"),
    ("ROAD", "Easy"), ("WIND", "Easy"),

    # Medium
    ("BRAIN", "Medium"), ("STREAM", "Medium"), ("PLANET", "Medium"), ("PYTHON", "Medium"),
    ("MONKEY", "Medium"), ("CANDLE", "Medium"), ("BUTTON", "Medium"), ("WINDOW", "Medium"),
    ("CHAIR", "Medium"), ("TABLE", "Medium"),

    # Hard
    ("KNIGHT", "Hard"), ("WIZARD", "Hard"), ("PUZZLER", "Hard"), ("JAZZMAN", "Hard"),
    ("QUIZZES", "Hard"), ("ZEPHYR", "Hard"), ("PHYSICS", "Hard"), ("MYSTERY", "Hard"),
    ("GULLIVER", "Hard"), ("EQUATOR", "Hard")
]

data = []

for i, (word, difficulty) in enumerate(words):
    letter_count = len(word)
    if difficulty == "Easy":
        est_time = random.randint(20, 40)
        difficulty_score = round(random.uniform(0.1, 0.3), 2)
    elif difficulty == "Medium":
        est_time = random.randint(40, 60)
        difficulty_score = round(random.uniform(0.4, 0.6), 2)
    else:  # Hard
        est_time = random.randint(60, 90)
        difficulty_score = round(random.uniform(0.7, 0.9), 2)

    data.append({
        "level_id": i,
        "target_word": word,
        "difficulty": difficulty,
        "letter_count": letter_count,
        "estimated_duration_sec": est_time,
        "difficulty_score": difficulty_score
    })

df = pd.DataFrame(data)
df.to_csv("../data/levels.csv", index=False)
print("levels.csv file with 30 levels has been created.")

