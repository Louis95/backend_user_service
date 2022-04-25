from app.main.models.user import UserModel
from app.main.schemas.user import UserSchema

USER_NOT_FOUND = "User not found."
USER_ALREADY_EXISTS = "User 'first_name: {} and  last_name: {}' Already exists."

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserService:

    @classmethod
    def save_new_user(cls, data):
        first_name = data['first_name']
        last_name = data['last_name']
        if UserModel.find_by_name(first_name) and UserModel.find_by_name(last_name):
            return {'message': USER_ALREADY_EXISTS.format(first_name, last_name)}, 400

        user_data = user_schema.load(data)
        user_data.save_to_db()

        return user_schema.dump(user_data), 201

    @classmethod
    def get_all_users(cls):
        return user_list_schema.dump(UserModel.find_all()), 200

    @classmethod
    def get_user_by_id(cls, user_id: int):
        user_data = UserModel.find_by_id(user_id)
        if user_data:
            return user_schema.dump(user_data)
        return {'message': USER_NOT_FOUND}, 404

    @classmethod
    def get_user_by_name(cls, name: str):
        user_data = UserModel.find_by_name(name)
        if user_data:
            return user_schema.dump(user_data)
        return {'message': USER_NOT_FOUND}, 404

    @classmethod
    def delete_user(cls, user_id: int):
        user_data = UserModel.find_by_id(user_id)
        if user_data:
            user_data.delete_from_db()
            return {'message': "User Deleted successfully"}, 200
        return {'message': USER_NOT_FOUND}, 404
