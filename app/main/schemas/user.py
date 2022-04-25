
from .. import ma
from app.main.models.user import UserModel
from app.main.schemas.email import EmailSchema
from app.main.schemas.phone_number import PhoneNumberSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    emails = ma.Nested(EmailSchema, many=True)
    phone_numbers = ma.Nested(PhoneNumberSchema, many=True)

    class Meta:
        model = UserModel
        load_instance = True
        include_fk = True
