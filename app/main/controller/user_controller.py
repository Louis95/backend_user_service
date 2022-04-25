from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import UserService


user_ns = UserDto.user_ns
_user = UserDto.user


class Users(Resource):
    @user_ns.doc("list_of_registered_users")
    def get(self):
        """List all registered users gd"""
        return UserService.get_all_users()

    @user_ns.response(201, "User successfully created.")
    @user_ns.doc("create a new user")
    @user_ns.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        user_data = request.json
        return UserService.save_new_user(user_data)


class User(Resource):
    @user_ns.doc("get a user given its identifier")
    @user_ns.marshal_with(_user)
    def get(self, user_id):
        """get a user given its identifier"""
        return UserService.get_user_by_id(user_id)

    @user_ns.doc("delete a user")
    def delete(self, user_id):
        """Delete a user with a given id"""
        return UserService.delete_user(user_id)


@user_ns.param("name", "The User name")
@user_ns.response(404, "User not found.")
class UserByName(Resource):
    @user_ns.doc("get a user by name")
    @user_ns.marshal_with(_user)
    def get(self, name):
        """get a user by name"""
        return UserService.get_user_by_name(name)

