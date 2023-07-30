#!/usr/bin/python3
""" Index """
from models.book import Book
'''from models.book_recommended import Recommended'''
from models.user import User
from models.storage.db_storage import DBStorage
from api.v1.views import app_views
from flask import jsonify, abort


storage = DBStorage()

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ Status of API """
    return jsonify({"status": "OK"}), 200 # type: ignore


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects() -> str:
    """ Retrieves the number of each objects by type """
    classes = ['Book', 'Recommended', 'User']
    names = ["books", "recommended", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs) # type: ignore


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def not_authorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      - raise a 401 error by using abort
    """
    return abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def page_forbidden() -> str:
    """ GET /api/v1/forbidded
    Return:
      - raise a 403 error by using abort
    """
    return abort(403)

