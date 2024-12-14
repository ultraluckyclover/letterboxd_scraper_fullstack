from config import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(100), nullable = False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    release_year = db.Column(db.String(4), nullable = False)
    description = db.Column(db.Text, nullable = True)
    movie_url = db.Column(db.String(200), nullable = False)
    img_url = db.Column(db.String(200), nullable = True)
 
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "releaseYear": self.release_year,
            "description": self.description,
            "movieUrl": self.movie_url,
            "imgUrl": self.img_url
        }