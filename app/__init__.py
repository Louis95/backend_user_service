from flask_restplus import Api
from flask import Blueprint, jsonify

from .main.controller.user_controller import Users, User, UserByName, user_ns
from .main.controller.email_controller import Email, Emails, email_ns
from .main.controller.phone_number_controller import PhoneNumber, PhoneNumbers, phone_number_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='User query backend',
          version='1.0',
          description='query user from the database'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(email_ns, path="/email")
api.add_namespace(phone_number_ns, path="/phone")

# user endpoints
user_ns.add_resource(Users, '/')
user_ns.add_resource(User, '/<int:user_id>')
user_ns.add_resource(UserByName, '/<string:name>')

# email endpoints
email_ns.add_resource(Emails, '/')
email_ns.add_resource(Email, '/<int:email_id>')

# phone number endpoints
phone_number_ns.add_resource(PhoneNumbers, '/')
phone_number_ns.add_resource(PhoneNumber, '/<int:phone_number_id>')

