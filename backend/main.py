from flask import request, jsonify
from config import app, db
from models import Movie
from routes import get_movies, create_movie, delete_movie

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)