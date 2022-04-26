import unittest

from app.main.models.user import UserModel
from app.main.models.phone_number import PhoneNumberModel
from typing import List
from app.test.fixtures import db, app
from flask_sqlalchemy import SQLAlchemy

from app.main.service.phone_number_service import PhoneNumberService


def create_test_users(db: SQLAlchemy):
    louis: UserModel = UserModel(first_name="louis", last_name="aso")
    penn: UserModel = UserModel(first_name="penn", last_name="muluh")
    db.session.add(louis)
    db.session.add(penn)
    db.session.commit()


def create_test_phone_number(db: SQLAlchemy):
    test_phone_number = PhoneNumberModel(phone_number="67364726354", user_id=1)
    db.session.add(test_phone_number)
    db.session.commit()


def test_get_all(db: SQLAlchemy):
    create_test_phone_number(db)
    results: List[UserModel] = PhoneNumberService.get_all_phone_numbers()

    assert len(results) == 2
    assert results[0][0]["phone_number"] == "67364726354"


def test_save_new_phone_number(db: SQLAlchemy):
    result = PhoneNumberService.save_new_phone_number({"phone_number": "7846572837", "user_id": 3})

    assert result[0]["phone_number"] == "7846572837"
    assert result[1] == 201


def test_update_phone_number(db: SQLAlchemy):
    create_test_phone_number(db)

    result = PhoneNumberService.update_phone_number(1, {"phone_number": "0987463746"})
    assert result[0]["phone_number"] == "0987463746"
