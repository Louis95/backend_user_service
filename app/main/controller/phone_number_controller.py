from flask import request
from flask_restplus import Resource

from ..util.dto import PhoneNumberDto
from ..service.phone_number_service import PhoneNumberService

phone_number_ns = PhoneNumberDto.phone_number_ns
_phone_number = PhoneNumberDto.phone_number
_update_phone_number = PhoneNumberDto.update_phone_number


class PhoneNumbers(Resource):
    @phone_number_ns.doc("list all available phone numbers")
    def get(self):
        """List all registered emails"""
        return PhoneNumberService.get_all_phone_numbers()

    @phone_number_ns.response(201, "Email successfully created.")
    @phone_number_ns.doc("create a new phone number")
    @phone_number_ns.expect(_phone_number, validate=True)
    def post(self):
        """Creates a new Phone number"""
        data = request.json
        return PhoneNumberService.save_new_phone_number(data)


class PhoneNumber(Resource):
    @phone_number_ns.response(201, "phone numbers successfully updated")
    @phone_number_ns.doc("Update an existing phone number")
    @phone_number_ns.expect(_update_phone_number, validate=True)
    def put(self, phone_number_id):
        data = request.json
        return PhoneNumberService.update_phone_number(phone_number_id, data)
