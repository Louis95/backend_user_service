from .. import ma
from app.main.models.user import UserModel
from app.main.models.email import EmailModel


class EmailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmailModel
        load_instance = True
        load_only = ("user",)
        include_fk = True
