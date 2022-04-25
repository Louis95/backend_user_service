from .. import db
from typing import List


class EmailModel(db.Model):
    __tablename__ = "emails"

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("UserModel", back_populates="emails")

    def __init__(self, email_address, user_id):
        self.email_address = email_address
        self.user_id = user_id

    def __repr__(self):
        return 'EmailModel(email_address=%s)' % self.email_address

    @classmethod
    def find_all(cls) -> List["EmailModel"]:
        return cls.query.all()

    @classmethod
    def find_by_email_address(cls, _email_address) -> "EmailModel":
        return cls.query.filter_by(email_address=_email_address).first()

    @classmethod
    def find_by_id(cls, _id) -> "EmailModel":
        return cls.query.filter_by(id=_id).first()

    def update_email(self) -> None:
        db.session.merge(self)
        db.session.commit()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
