#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Books"""
from models.book import Book
from models.storage.db_storage import DBStorage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


storage = DBStorage()

@app_views.route('/books', methods=['GET'], strict_slashes=False)
@swag_from('documentation/book/all_books.yml')
def get_books():
    """
    Retrieves a list of all books
    """
    all_books = storage.all(Book).values()
    list_books = []
    for book in all_books:
        list_books.append(book.to_dict())
    return jsonify(list_books)


@app_views.route('/books/<book_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/book/get_book.yml', methods=['GET'])
def get_book(book_id):
    """ Retrieves a book """
    book = storage.get('Book', book_id)
    if not book:
        abort(404)

    return jsonify(book.to_dict())


@app_views.route('/books/<book_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/book/delete_book.yml', methods=['DELETE'])
def delete_book(book_id):
    """
    Deletes a book  Object
    """

    book = storage.get('Book', book_id)

    if not book:
        abort(404)

    storage.delete(book)
    storage.save(None)

    return make_response(
            jsonify(
                {'Deleted': book.title + ' ' + 'by' + ' ' + book.author}
                ), 200)


@app_views.route('/books', methods=['POST'], strict_slashes=False)
@swag_from('documentation/book/post_book.yml', methods=['POST'])
def post_book():
    """
    Creates a book
    """
    title = request.form.get('title')
    author = request.form.get('author')
    category = request.form.get('category')
    published = request.form.get('published')

    data = {}
    if not title and not isinstance(title, str):
        abort(406, description="Missing title")
    else:
        data['title'] = title
    if not author and not isinstance(author, str):
        abort(406, description="Missing author")
    else:
        data['author'] = author
    if not category and not isinstance(category, str):
        abort(406, description="Missing category")
    else:
        data['category'] = category
    if not published and not isinstance(published, int):
        abort(406, description="Missing publishe year or not integer")
    else:
        data['published'] = published

    db_books = list(storage.all(Book).values())
    if db_books:
        for book in db_books:
            if book.title == title:
                return abort(409,
                        description='title already exists')

    instance = Book(**data)
    storage.save(instance)
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/books/<book_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/book/put_book.yml', methods=['PUT'])
def put_book(book_id):
    """
    Updates a book
    """
    title = request.form.get('title')
    published = request.form.get('published')
    category = request.form.get('category')

    data = {}
    if not title and not isinstance(title, str):
        abort(406,
                description="Missing title or not a string")
    else:
        data['title'] = title
    if not published and not isinstance(published, int):
        abort(406,
                description="Missing published year or not an integer")
    else:
        data['published'] = published
    if not category and not isinstance(category, str):
        abort(406,
                description="Missing category")

    book = storage.get('Book', book_id)

    if not book:
        abort(404)

    if book.category == category:
        for key, value in data.items():
            print (key, value)
            setattr(book, key, value)
            storage.save(book)
    return make_response(jsonify(book.to_dict()), 200)
