#!/usr/bin/python3
"""
User creation class
"""
from models.bookmotion_base import BookMotionBase, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex
from os import getenv


class Book(BookMotionBase, Base):
    """Defines attributes for user creation"""
    __tablename__ = "books"
    if getenv("BOOK_TYPE_STORAGE") == "db":
        author = Column(String(128), nullable=True)
        title = Column(String(128), nullable=True)
        category = Column(String(128))
        publication_year = Column(Integer, nullable=True)

    else:
        author=""
        title=""
        category=""
        publication_year=0

    def recommended(self):
        """getter attribute returns the list of Recommended books"""
        from models.book_recommended import Recommended
        rec_list = []
        all_recommend = models.storage.all(Recommended)
        for rec in all_recommend.values():
            if rec.book_id == self.id:
                rec_list.append(rec)
        return rec_list
