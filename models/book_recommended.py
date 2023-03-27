#!/usr/bin/python3
"""
Defines review class
"""
from sqlalchemy import Column, String, ForeignKey
from models.bookmotion_base import BookMotionBase, Base


class Recommended(BookMotionBase, Base):
    '''
        Implementation for the Recommended.
    '''
    __tablename__ = "recommended"
    text = Column(String(1024), nullable=True)
    book_id = Column(String(60), ForeignKey("books.id"), nullable=True)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=True)
    '''else:
        book_id = ""
        user_id = ""
        text = ""
    '''