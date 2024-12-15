from config import app, db
from flask import request, jsonify
from models import Movie

# get all movies

@app.route("/api/movies", methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    json_movies = list(map(lambda x: x.to_json(), movies))
    return jsonify({"movies": json_movies}), 200

# get single movie

@app.route("/api/movies/<int:id>", methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)

    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    return movie.to_json(), 200

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

# update movie
# I think I will only use this to add descriptions fetched from the TMDB API

@app.route('/api/movies/<int:id>', methods = ['PATCH'])
def update_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json

    movie.title = data.get('title', movie.title)
    movie.release_year = data.get('releaseYear', movie.release_year)
    movie.description = data.get('description', movie.description)
    movie.img_url = data.get('imgUrl', movie.img_url)
    movie.movie_url = data.get('movieUrl', movie.movie_url)

    db.session.commit()

    return jsonify({"message": "User updated"}), 200

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
    

