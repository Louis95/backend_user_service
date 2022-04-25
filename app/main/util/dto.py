from flask_restplus import Namespace, fields, Api
from app.main.models.phone_number import PhoneNumberModel
from app.main.models.email import EmailModel


class UserDto:
    user_ns = Namespace('users', description='user related operations')
    user = user_ns.model('UserModel', {
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
    })


class EmailDto:
    email_ns = Namespace('emails', description='email related operations')
    email = email_ns.model('EmailModel', {
        'email_address': fields.String(required=True, description="email address"),
        'user_id': fields.Integer(required=True, description="user id")
    })

    update_email = email_ns.model('UpdateEmail', {
        'email_address': fields.String(required=True, description="email address")
    })


class PhoneNumberDto:
    phone_number_ns = Namespace('phone numbers', description='phone numbers related operations')
    phone_number = phone_number_ns.model('PhoneNumberModel', {
        'phone_number': fields.String(required=True, description=" phone number"),
        'user_id': fields.Integer(required=True, description="user id")
    })

    update_phone_number = phone_number_ns.model('updatePhoneNumber', {
        'phone_number': fields.String(required=True, description=" phone number"),
    })
