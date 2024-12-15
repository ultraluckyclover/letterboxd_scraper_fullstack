from config import app, db
from routes import get_movies, get_movie, create_movie, delete_movie 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port= 8000, debug = True)