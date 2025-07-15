from sqlalchemy.orm import Session
from . import models

def get_detections(db: Session, limit: int = 10):
    return db.query(models.ImageDetection).limit(limit).all()
