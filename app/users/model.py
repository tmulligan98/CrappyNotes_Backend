from sqlalchemy.orm import relationship
from app.db import db

class UserModel(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(50), nullable=False, unique=True, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    notes = relationship("NoteModel")

    def to_dict(self):
        return {
            "id": self.id, 
            "username": self.username,
            "email": self.email
        }