#!/usr/bin/python3
"""
User creation class
"""
from models.bookmotion_base import BookMotionBase, Base
from sqlalchemy import Column, String


class User(BookMotionBase, Base):
    """Defines attributes for user creation
    """
    __tablename__ = "users"
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password =  Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name =  Column(String(128), nullable=True)
    
    def __str__(self):
        """
        Return string representation of the model
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))
        
    '''else:
        email = ""
        username = ""
        password = ""
        first_name = ""
        last_name = ""
    '''
