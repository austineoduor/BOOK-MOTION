#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<email>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(email):
    """ Retrieves an user """
    user = storage.get(User, email)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/email', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(email):
    """
    Deletes a user Object
    """

    user = storage.get(User, email)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        abort(400, description="Missing email")
    if not password:
        abort(400, description="Missing password")

    data = {}
    data['email'] = email
    data['password'] = password
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<email>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(email):
    """
    Updates a user
    """
    user = storage.get(User, email)

    if not user:
        abort(404)

    email = request.form.get('email')
    password = request.form.get('password')
    
    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = {}
    data['email'] = email
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
