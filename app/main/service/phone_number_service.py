from typing import Dict, Optional
from app.main import db
from app.main.models.phone_number import PhoneNumberModel
from app.main.schemas.phone_number import PhoneNumberSchema
from flask import jsonify

PHONE_NUMBER_NOT_FOUND = "Phone number not found."
PHONE_NUMBER_ALREADY_EXISTS = "Phone number {}' Already exists."

phone_number_schema = PhoneNumberSchema()
phone_number_list_schema = PhoneNumberSchema(many=True)

RESULT_PER_PAGE = 100


class PhoneNumberService:

    @classmethod
    def get_all_phone_numbers(cls):
        return phone_number_list_schema.dump(PhoneNumberModel.find_all()), 200

    @classmethod
    def save_new_phone_number(cls, data):
        phone_number = data['phone_number']
        if PhoneNumberModel.find_by_phone_number(phone_number):
            return {'message': PHONE_NUMBER_ALREADY_EXISTS.format(phone_number)}, 400

        phone_number_data = phone_number_schema.load(data)
        phone_number_data.save_to_db()

        return phone_number_schema.dump(phone_number_data), 201

    @classmethod
    def update_phone_number(cls, phone_number_id, data):
        phone_number_to_update = PhoneNumberModel.find_by_id(phone_number_id)
        if not phone_number_to_update:
            return {'message': PHONE_NUMBER_NOT_FOUND}, 404

        phone_number_to_update.phone_number = data["phone_number"]
        phone_number_to_update.update_phone_number()

        return phone_number_schema.dump(phone_number_to_update), 201
