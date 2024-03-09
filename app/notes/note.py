from flask_restx import Resource, reqparse
from flask import abort
from .model import NoteModel
from app.db import db
from datetime import datetime

class Note(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('note', type=str, required=True, help="This field cannot be left blank", location="args")

    def __init__(self) -> None:
        # Carry out some initialisation (logging for example)
        pass

    def get(self, id: str) -> str:
       
        try:
            note = NoteModel.query.get(id)
            if note:
                return {"notes": note}, 200
            
            abort(404, "Note not found")
        except Exception as e:
            abort(500, "Internal Error")

    def post(self, note: str) -> str:

        try:
            new_note = NoteModel(note=note, timestamp=datetime.now())
            db.session.add(new_note)
            db.session.commit()
                
            return {'message': 'Added Note'}, 200
            
        except Exception as e:
            abort(500, "Internal Error")
        
    def delete(self, id: str) -> str:

        try:
            note = NoteModel.query.get(id)
            db.session.delete(note)
            db.session.commit()
                
            return {'message': 'Added Note'}, 200
            
        except Exception as e:
            abort({"message": "Internal Error"}, 500)
        

class NoteList(Resource):

    def get(self):
        try:
            notes = NoteModel.query.all()
            return {'message': notes}, 200
            
        except Exception as e:
            abort({"message": "Internal Error"}, 500)