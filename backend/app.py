# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from flask_migrate import Migrate

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///letterboxd.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# import routes

# with app.app_context():
#     db.create_all()

# if __name__ == '__main__':
#     app.run(debug = True)
