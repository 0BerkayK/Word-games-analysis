import pandas as pd
import random
from datetime import datetime, timedelta

player_ids = [f"player_{i:03d}" for i in range(100)]
segments = ["casual", "regular", "hardcore"]
session_data = []

for player_id in player_ids:
    segment = random.choice(segments)
    num_sessions = random.randint(5, 15)
    played_levels = random.sample(range(30), num_sessions)

    for level_id in played_levels:
        # Simulated attempts (casual users need more attempts)
        base_attempts = random.randint(1, 3)
        if segment == "casual":
            attempts = base_attempts + random.choice([0, 1])
        elif segment == "hardcore":
            attempts = max(1, base_attempts - 1)
        else:
            attempts = base_attempts

        completed = random.random() < 0.85  # 85% başarı ihtimali
        completion_time = random.randint(20, 90) if completed else None
        play_date = datetime.today() - timedelta(days=random.randint(0, 30))

        session_data.append({
            "player_id": player_id,
            "player_segment": segment,
            "level_id": level_id,
            "completion_time_sec": completion_time,
            "attempts": attempts,
            "completed": completed,
            "date": play_date.strftime("%Y-%m-%d")
        })

df_sessions = pd.DataFrame(session_data)
df_sessions.to_csv("../data/player_session.csv", index=False)
print("player_session.csv dosyası oluşturuldu.")
