from typing import Dict, Optional
from app.main import db
from app.main.models.email import EmailModel
from app.main.schemas.email import EmailSchema
from flask import jsonify

USER_NOT_FOUND = "Email not found."
EMAIL_ADDRESS_ALREADY_EXISTS = "Email address {}' Already exists."

email_schema = EmailSchema()
email_list_schema = EmailSchema(many=True)

RESULT_PER_PAGE = 100


class EmailService:

    @classmethod
    def get_all_emails(cls):
        return email_list_schema.dump(EmailModel.find_all()), 200

    @classmethod
    def save_new_email(cls, data):
        email_address = data['email_address']
        if EmailModel.find_by_email_address(email_address):
            return {'message': EMAIL_ADDRESS_ALREADY_EXISTS.format(email_address)}, 400

        email_data = email_schema.load(data)
        email_data.save_to_db()

        return email_schema.dump(email_data), 201

    @classmethod
    def update_email(cls, data, email_id):
        email_to_update = EmailModel.find_by_id(email_id)
        if not email_to_update:
            return {'message': USER_NOT_FOUND}, 404

        email_to_update.email_address = data["email_address"]
        email_to_update.update_email()

        return email_schema.dump(email_to_update), 201
