#!/usr/bin/env python3
from models.storage.db_storage import DBStorage
from models.book import Book

st = DBStorage()
data = {
    'author': 'Roland',
    'title': 'control',
    'category': 'engineering',
    'published': 2001
    }
if __name__ == '__main__':
    book = Book(**data)
    #print(users)
    st.save(book)
    print(st.all('Book'))
    print(st.count('Book'))