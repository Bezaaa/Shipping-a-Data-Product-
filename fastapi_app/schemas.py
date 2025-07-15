from pydantic import BaseModel

class ImageDetectionOut(BaseModel):
    id: str
    image_path: str
    class_: int
    confidence: float
    timestamp: str

    class Config:
        orm_mode = True
