from flask_restful import Resource, reqparse
from flask import abort
from json import dump, dumps, load
from datetime import datetime
import os

SAMPLE_JSON = "./notes/notes.json"



class Note(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('note', type=str, required=True, help="This field cannot be left blank", location="args")

    def __init__(self) -> None:
        # Carry out some initialisation (logging for example)
        pass

    def get(self, id: str) -> str:
       
        try:
            with open(SAMPLE_JSON, "r") as f:

                data = load(f)

                item = data[id]

                if item:
                    return {"notes": item}, 200
                
                abort(404, "Note not found")
        except Exception as e:
            abort(500, "Internal Error")

    def post(self, id: str) -> str:

        try:
            data = None

            with open(SAMPLE_JSON, "r") as file:
                data = load(file)

            note = Note.parser.parse_args()["note"]

            data[id] = note

            with open(SAMPLE_JSON, "w") as file:
                dump(data, file, indent=2)
                
            return {'message': 'Added Note'}, 200
            
        except Exception as e:
            abort(500, "Internal Error")
        
    def delete(self, id: str) -> str:

        try:
            data = None

            with open(SAMPLE_JSON, "r") as file:
                data = load(file)

            if id in data:
                del data[id]
            else:
                abort(404, "Note not found")


            with open(SAMPLE_JSON, "w") as file:
                dump(data, file, indent=2)
                
            return {'message': 'Added Note'}, 200
            
        except Exception as e:
            abort({"message": "Internal Error"}, 500)
        

class NoteList(Resource):

    def get(self):
        with open(SAMPLE_JSON, "r") as file:
                data = load(file)
                return {"notes":list(data.values())}, 200