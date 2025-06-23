import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    profile_picture = Column(String(250))
    bio = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    posts = relationship('Post', backref='author')
    comments = relationship('Comment', backref='author')
    following = relationship('Follower', foreign_keys='Follower.follower_id', backref='follower_user')
    followers = relationship('Follower', foreign_keys='Follower.followed_id', backref='followed_user')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    image_url = Column(String(250), nullable=False)
    caption = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    comments = relationship('Comment', backref='post')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Follower(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    followed_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Dibuja el diagrama ERD en diagram.png
try:
    render_er(Base, 'diagram.png')
    print("¡Diagrama creado exitosamente!")
except Exception as e:
    print("Hubo un problema al generar el diagrama:", e)
