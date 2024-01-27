from flask import Flask, jsonify, request
from app.notes import Note, NoteList
from flask_restful import Api

VERSION_STR = "v1"

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Note, f"/{VERSION_STR}/notes/<id>")
api.add_resource(NoteList, f"/{VERSION_STR}/notes")

@app.errorhandler(404)
def handle_not_found_error(error):
    return {"error": "Not Found", "message": str(error.description)}, 404

@app.errorhandler(404)
def handle_internal_error():
    return {"error": "Internal Error"}, 500

if __name__ == "__main__":
    app.run(debug=True)