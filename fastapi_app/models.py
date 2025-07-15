from sqlalchemy import Column, Integer, String, Float
from .database import Base

class ImageDetection(Base):
    __tablename__ = "fct_image_detections"

    id = Column(String, primary_key=True, index=True)
    image_path = Column(String)
    class_ = Column("class", Integer)
    confidence = Column(Float)
    timestamp = Column(String)
