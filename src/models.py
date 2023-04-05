# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy DB object
db = SQLAlchemy()

# Define Movie model
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Movie {self.id}: {self.title} ({self.year})>"
