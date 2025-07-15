# yolo/detect_objects.py
from ultralytics import YOLO
import os
import json
import uuid
from datetime import datetime

IMAGE_DIR = "data/raw/images"
OUTPUT_JSON = "data/enriched/image_detections.json"

model = YOLO("yolov8n.pt")  

def detect_objects():
    results = []
    for root, _, files in os.walk(IMAGE_DIR):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(root, file)
                preds = model(file_path)[0]

                for det in preds.boxes:
                    results.append({
                        "id": str(uuid.uuid4()),
                        "image_path": file_path,
                        "class": int(det.cls[0].item()),
                        "confidence": float(det.conf[0].item()),
                        "timestamp": datetime.now().isoformat()
                    })

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Detections saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    detect_objects()
