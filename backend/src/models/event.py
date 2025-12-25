"""
    1. Create Event Model

        - EventName, Description, Date, CreatedAt, UpdatedAt, Place, EventType(Genre), Era
"""

from src.extension import db
import uuid
from enum import Enum
from sqlalchemy.sql import func

class Era(Enum):

    PREHISTORIC = "PREHISTORIC"
    CLASSICAL = "CLASSICAL"
    MIDDLEAGE = "MIDDLEAGE"
    EARLYMODERN = "EARLYMODERN"
    MODERN  = "MODERN"


class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    era = db.Column(db.Enum(Era), default=Era.MODERN)

    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "era": self.era.value,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }