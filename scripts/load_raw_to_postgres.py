import json
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Connect to Postgres
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="medical_data",
    user="postgres",
    password="postgres"  # Match Docker credentials
)
cur = conn.cursor()

# Create raw table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS raw_telegram_messages (
    id SERIAL PRIMARY KEY,
    channel TEXT,
    message_id INT,
    text TEXT,
    date TIMESTAMP,
    raw JSONB
)
""")

conn.commit()

# Load messages from raw JSON
raw_dir = "data/raw/telegram_messages"
for root, _, files in os.walk(raw_dir):
    for file in files:
        if file.endswith(".json"):
            channel = file.replace(".json", "")
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                messages = json.load(f)
                for msg in messages:
                    cur.execute("""
                        INSERT INTO raw_telegram_messages (channel, message_id, text, date, raw)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (
                        channel,
                        msg.get("id"),
                        msg.get("message", ""),
                        msg.get("date"),
                        json.dumps(msg)
                    ))

conn.commit()
cur.close()
conn.close()
