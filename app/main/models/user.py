from .. import db, flask_bcrypt
from typing import List


class UserModel(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)

    emails = db.relationship("EmailModel", lazy="dynamic", primaryjoin="UserModel.id == EmailModel.user_id",
                             back_populates="user", cascade='all, delete-orphan')
    phone_numbers = db.relationship("PhoneNumberModel", lazy="dynamic",
                                    primaryjoin="UserModel.id == PhoneNumberModel.user_id", back_populates="user", cascade='all, delete-orphan')

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return "<UserModel '{}'>".format(self.first_name, self.last_name, self.emails, self.phone_numbers)

    @classmethod
    def find_by_name(cls, name) -> "UserModel":
        return cls.query.filter((cls.first_name == name) | (cls.last_name == name)).first()

    @classmethod
    def find_by_id(cls, _id) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
