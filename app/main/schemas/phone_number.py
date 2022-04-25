from .. import ma
from app.main.models.user import UserModel
from app.main.models.phone_number import PhoneNumberModel


class PhoneNumberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PhoneNumberModel
        load_instance = True
        load_only = ("user",)
        include_fk = True
