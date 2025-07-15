from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database, crud, schemas

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/detections", response_model=list[schemas.ImageDetectionOut])
def read_detections(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detections(db, limit=limit)
