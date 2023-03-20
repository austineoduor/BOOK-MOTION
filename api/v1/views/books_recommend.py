#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.book_recommended import Recommended
from models.book import Book
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/books/<book_id>/reviews', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/books/get_books.yml', methods=['GET'])
def get_books(book_id):
    """
    Retrieves the list of all Review objects of a Book
    """
    book = storage.get(Book, book_id)

    if not book:
        abort(404)

    recommend = [recommend.to_dict() for recommend in book.recommended]

    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/reviews/get_review.yml', methods=['GET'])
def get_review(review_id):
    """
    Retrieves a Review object
    """
    recommend = storage.get(Recommended, recommend_id)
    if not recommend:
        abort(404)

    return jsonify(recommend.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/reviews/delete_reviews.yml', methods=['DELETE'])
def delete_review(recommend_id):
    """
    Deletes a Review Object
    """

    rec = storage.get(Recommended, recommend_id)

    if not rec:
        abort(404)

    storage.delete(rec)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/books/<book_id>/reviews', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/reviews/post_reviews.yml', methods=['POST'])
def post_review(book_id):
    """
    Creates a Review
    """
    book = storage.get(Book, book_id)

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
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/reviews/put_reviews.yml', methods=['PUT'])
def put_review(recommend_id):
    """
    Updates a Review
    """
    rec = storage.get(Recommended, recommend_id)

    if not rec:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'book_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(recommend, key, value)
    storage.save()
    return make_response(jsonify(rec.to_dict()), 200)
