from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    favorites = db.relationship('Favorite', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f"<User {self.username}>"

    # ... existing fields ...
    watch_later = db.relationship('WatchLater', backref='user', lazy=True)
    # ...    


class Content(db.Model):
    __tablename__ = 'contents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)
    content_type = db.Column(db.String(20), nullable=False)  # movie, series, animation
    genre = db.Column(db.String(50), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    
    # Relationship
    favorites = db.relationship('Favorite', backref='content', lazy=True)
    
    def __repr__(self):
        return f"<Content {self.title}>"

    # ... existing fields ...
    watch_later = db.relationship('WatchLater', backref='content', lazy=True)
    # ...


    

class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Favorite {self.user_id}:{self.content_id}>"
    

class WatchLater(db.Model):
    __tablename__ = 'watch_later'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<WatchLater {self.user_id}:{self.content_id}>"
