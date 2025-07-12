import os
import json
import logging
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

CHANNELS = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma",
    "https://t.me/CheMed123"
]

TODAY = datetime.now().strftime("%Y-%m-%d")
BASE_PATH = f"data/raw/telegram_messages/{TODAY}"
os.makedirs(BASE_PATH, exist_ok=True)

logging.basicConfig(filename="telegram_scraper.log", level=logging.INFO)

client = TelegramClient("session", API_ID, API_HASH)

def start_client():
    try:
        client.start()
    except SessionPasswordNeededError:
        pw = input("Two-step verification enabled. Please enter your Telegram password: ")
        client.start(password=pw)

def scrape():
    print("Telegram client started successfully.")
    for channel in CHANNELS:
        try:
            print(f"Scraping channel: {channel}")
            entity = client.get_entity(channel)
            messages = []

            for message in client.iter_messages(entity, limit=10):
                msg = {
                    "id": message.id,
                    "text": message.text,
                    "date": message.date.isoformat() if message.date else None,
                    "has_media": bool(message.media),
                    "photo": None
                }

                if message.photo:
                    img_name = f"{entity.username}_{message.id}.jpg"
                    img_path = os.path.join(BASE_PATH, img_name)
                    client.download_media(message.photo, img_path)
                    msg["photo"] = img_path

                messages.append(msg)

            out_path = os.path.join(BASE_PATH, f"{entity.username}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(messages, f, indent=2, ensure_ascii=False)

            print(f"Saved {len(messages)} messages from {channel} to {out_path}")
            logging.info(f"Scraped {len(messages)} messages from {channel}")

        except Exception as e:
            print(f"Error scraping {channel}: {e}")
            logging.error(f"Error scraping {channel}: {e}")

if __name__ == "__main__":
    start_client()
    scrape()
    client.disconnect()
    print("Scraping script finished.")
