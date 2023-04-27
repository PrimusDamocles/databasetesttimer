from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

db = SQLAlchemy()

class Posts(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    message = Column(String(128), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
