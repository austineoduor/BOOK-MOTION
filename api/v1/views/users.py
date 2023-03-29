#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models.storage.db_storage import DBStorage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request, render_template, json
from flasgger.utils import swag_from


storage = DBStorage()

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


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """ Retrieves one user by id """
    _id = str(user_id)
    user = storage.get('User', _id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user Object
    """

    user = storage.get('User', user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save(None)

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a user
    """
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    if not username:
        abort(400, description="Missing username")
    if not email:
        abort(400, description="Missing email")
    if not password:
        abort(400, description="Missing password")
    all_users = list(storage.all(User).values())
    if all_users:
        for users in all_users:
            if users.email == email:
                return abort(409)
    data = {}
    data['username'] = username
    data['email'] = email
    data['password'] = password
    instance = User(**data)
    storage.save(instance)
    return make_response(instance.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get('User', user_id)
    if not user:
        abort(404)

    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    data = {}
    print(user)
    if user.email == email:
        data['first_name'] = first_name
        data['last_name'] = last_name
    else:
        return abort(404)
    for key, value in data.items():
        setattr(user, key, value)
        storage.save(user)
    return make_response(jsonify(user.to_dict()), 200)
