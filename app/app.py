from flask import Flask
from app.notes import Note, NoteList
from flask_restx import Api
from app.db import db

VERSION_STR = "v1"

app = Flask(__name__)
api = Api(app, title='CrappyNotes Backend',
    description='A thin database wrapper...')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
with app.app_context():
    db.init_app(app)
    db.create_all()  

api.add_resource(Note, f"/{VERSION_STR}/notes/<id>")
api.add_resource(NoteList, f"/{VERSION_STR}/notes")

@app.errorhandler(404)
def handle_not_found_error(error):
    return {"error": "Not Found", "message": str(error.description)}, 404

@app.errorhandler(500)
def handle_internal_error():
    return {"error": "Internal Error"}, 500

if __name__ == "__main__":
    app.run(debug=True)