#!/usr/bin/python3
'''
 Creating a unique FileStorage
 instance for the application
'''
from models.storage.file_storage import FileStorage
from models.storage.db_storage import DBStorage
from os import getenv
from models.bookmotion_base import BookMotionBase
from models.user import User
from models.book import Book
from models.book_recommended import Recommended


if getenv("BOOK_TYPE_STORAGE") == "db":
    Storage = DBStorage()
else:
    Storage = FileStorage()

storage.reload()
