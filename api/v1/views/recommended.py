#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.book_recommended import Recommended
from models.book import Book
from models.user import User
from models.storage.db_storage import DBStorage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


storage = DBStorage()

@app_views.route('/recommendend', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/recommend/get_recommends.yml', methods=['GET'])
def get_rec_books(book_id):
    """
    Retrieves the list of all Recommended Books
    """
    book = storage.all(Recommended).values()
    if not book:
        abort(404)

    recommend = [recommend.to_dict() for recommend in book.recommended]

    return jsonify(recommend)


@app_views.route('/recommend/<recommend_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/recommend/get_recommend.yml', methods=['GET'])
def all_rec_book(recommend_id):
    """
    Retrieves a Review object
    """
    recommend = storage.get('Recommended', recommend_id)
    if not recommend:
        abort(404)

    return jsonify(recommend.to_dict())


@app_views.route('/recommend/<recommend_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/reviews/delete_recommend.yml', methods=['DELETE'])
def delete_rec_book(recommend_id):
    """
    Deletes a Review Object
    """

    rec = storage.get('Recommended', recommend_id)

    if not rec:
        abort(404)

    storage.delete(rec)
    storage.save(None)

    return make_response(jsonify({'Deleted': book.id}), 200)


@app_views.route('/books/<book_id>/recommend', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/recommend/post_recommend.yml', methods=['POST'])
def post_rec_book(book_id):
    """
    Creates a Recommended
    """
    book = storage.get('Book', book_id)

    if not book:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])

    if not user:
        abort(404)

    if 'text' not in request.get_json():
        abort(400, description="Missing text")

    data['book_id'] = book_id
    instance = Recommended(**data)
    storage.save(instance)
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/recommend/<recommend_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/recommend/put_recommend.yml', methods=['PUT'])
def put_rec_book(recommend_id):
    """
    Updates a Recommend
    """
    rec = storage.get('Recommended', recommend_id)

    if not rec:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'book_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(Recommended, key, value)
    storage.save()
    return make_response(jsonify(rec.to_dict()), 200)
