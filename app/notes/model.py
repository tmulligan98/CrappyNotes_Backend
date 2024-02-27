from datetime import datetime
from app.db import db
from app.users import UserModel

class NoteModel(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    note = db.Column(db.String(250), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.username))

    def to_dict(self):
        return {
            "id": self.id, 
            "note": self.note,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }