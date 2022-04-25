from .. import db
from typing import List


class PhoneNumberModel(db.Model):
    __tablename__ = "phone_numbers"

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("UserModel", back_populates="phone_numbers")

    def __init__(self, phone_number, user_id):
        self.phone_number = phone_number
        self.user_id = user_id

    def __repr__(self):
        return 'PhoneNumberModel(number_number=%s)' % self.phone_number

    @classmethod
    def find_by_phone_number(cls, _phone_number) -> "PhoneNumberModel":
        return cls.query.filter_by(phone_number=_phone_number).first()

    @classmethod
    def find_by_id(cls, _id) -> "PhoneNumberModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["PhoneNumberModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def update_phone_number(self) -> None:
        db.session.merge(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
