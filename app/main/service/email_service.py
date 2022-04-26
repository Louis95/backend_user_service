from typing import Dict, Optional
from app.main import db
from app.main.models.email import EmailModel
from app.main.schemas.email import EmailSchema
import re

USER_NOT_FOUND = "Email not found."
EMAIL_ADDRESS_ALREADY_EXISTS = "Email address {}' Already exists."
INVALID_EMAIL_ADDRESS = "Invalid Email address. Please enter a valid email address"

email_schema = EmailSchema()
email_list_schema = EmailSchema(many=True)

RESULT_PER_PAGE = 100


class EmailService:

    @staticmethod
    def get_all_emails():
        return email_list_schema.dump(EmailModel.find_all()), 200

    @staticmethod
    def save_new_email(data):
        email_address = data['email_address']
        if EmailModel.find_by_email_address(email_address):
            return {'message': EMAIL_ADDRESS_ALREADY_EXISTS.format(email_address)}, 400

        if not EmailService.email_validation(email_address):
            return {'message': INVALID_EMAIL_ADDRESS}, 400

        email_data = email_schema.load(data)
        email_data.save_to_db()

        return email_schema.dump(email_data), 201

    @staticmethod
    def update_email(data, email_id):
        email_address = data["email_address"]
        email_to_update = EmailModel.find_by_id(email_id)
        if not email_to_update:
            return {'message': USER_NOT_FOUND}, 404

        if not EmailService.email_validation(email_address):
            if not EmailService.email_validation(email_address):
                return {'message': INVALID_EMAIL_ADDRESS}, 400

        email_to_update.email_address = email_address
        email_to_update.update_email()

        return email_schema.dump(email_to_update), 201

    @staticmethod
    def email_validation(email_address):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex, email_address):
            return True
        else:
            return False
