from flask import request
from flask_restplus import Resource

from ..util.dto import EmailDto
from ..service.email_service import EmailService


email_ns = EmailDto.email_ns
_email = EmailDto.email
_update_email = EmailDto.update_email


class Emails(Resource):
    @email_ns.doc("list all available emails")
    def get(self):
        """List all registered emails"""
        return EmailService.get_all_emails()

    @email_ns.response(201, "Email successfully created.")
    @email_ns.doc("create a new email")
    @email_ns.expect(_email, validate=True)
    def post(self):
        """Creates a new Email"""
        data = request.json
        return EmailService.save_new_email(data)


class Email(Resource):
    @email_ns.response(201, "Email successfully updated")
    @email_ns.doc("Update an existing email")
    @email_ns.expect(_update_email, validate=True)
    def put(self, email_id):
        data = request.json
        return EmailService.update_email(data, email_id)


