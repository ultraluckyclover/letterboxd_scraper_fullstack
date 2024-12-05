from app import app, db
from flask import request, jsonify
from models import Movie

# get all movies

@app.route("/api/movies", methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    result = [movie.to_json() for movie in movies]
    return jsonify(result), 200

# add a movie

@app.route('/api/movies', methods=["POST"])
def create_movie():
    try:
        data = request.json

        # Validation
        required_fields = ["title", "releaseYear", "movieUrl"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f'Missing required field: {field}'}), 400

        title = data.get('title')
        release_year = data.get('releaseYear')
        description = data.get('description')
        img_url = data.get('imgUrl')
        movie_url = data.get('movieUrl')

        new_movie = Movie(title = title, 
                          release_year = release_year, 
                          description = description, 
                          movie_url = movie_url,
                          img_url = img_url)
        
        db.session.add(new_movie)
        db.session.commit()
        return jsonify(new_movie.to_json()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# delete a movie

@app.route('/api/movies/<int:id>', methods = ["DELETE"])
def delete_movie(id):
    try:
        movie = Movie.query.get(id)
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404
        db.session.delete(movie)
        db.session.commit()
        return jsonify({"msg": "Movie removed from database"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

