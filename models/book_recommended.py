#!/usr/bin/python3
"""
Defines review class
"""
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.bookmotion_base import BookMotionBase, Base


class Recommended(BookMotionBase, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "recommended"
    if getenv("STORAGE") == "db":
        text = Column(String(1024), nullable=True)
        book_id = Column(String(60), ForeignKey("books.id"), nullable=True)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=True)
    else:
        book_id = ""
        user_id = ""
        text = ""
