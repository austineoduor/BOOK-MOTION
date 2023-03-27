#!/usr/bin/python3
"""
User creation class
"""
from models.bookmotion_base import BookMotionBase, Base
from sqlalchemy import Column, Integer, String


class Book(BookMotionBase, Base):
    """Defines attributes for user creation"""
    __tablename__ = "books"
    author = Column(String(128), nullable=True)
    title = Column(String(128), nullable=True)
    category = Column(String(128))
    published = Column(Integer, nullable=True)

    '''else:
        author=""
        title=""
        category=""
        publication_year=0
    '''
    def recommended(self):
        """getter attribute returns the list of Recommended books"""
        from models.book_recommended import Recommended
        from models.storage.db_storage import DBStorage as storage
        rec_list = []
        all_recommend = storage.all(Recommended)
        for rec in all_recommend.values():
            if rec.book_id == self.id:
                rec_list.append(rec)
        return rec_list
