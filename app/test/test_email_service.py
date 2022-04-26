from app.main.models.user import UserModel
from app.main.models.email import EmailModel
from typing import List
from app.test.fixtures import db, app
from flask_sqlalchemy import SQLAlchemy

from app.main.service.email_service import EmailService


def create_test_email(db: SQLAlchemy):
    test_email = EmailModel(email_address="test@gmail.com", user_id=1)
    db.session.add(test_email)
    db.session.commit()


def test_get_all(db: SQLAlchemy):
    create_test_email(db)
    results: List[UserModel] = EmailService.get_all_emails()

    assert len(results) == 2
    assert results[0][0]["email_address"] == "test@gmail.com"


def test_save_new_email(db: SQLAlchemy):
    result = EmailService.save_new_email({"email_address": "test_user@gmail.com", "user_id": 3})

    assert result[0]["email_address"] == "test_user@gmail.com"
    assert result[1] == 201


def test_update_phone_number(db: SQLAlchemy):
    create_test_email(db)

    result = EmailService.update_email({"email_address": "loui@gmail.com"}, 1)
    assert result[0]["email_address"] == "loui@gmail.com"


def test_email_validation(db: SQLAlchemy):
    valid_email = "test-email@gmail.com"
    valid_email_result = EmailService.email_validation(valid_email)
    invalid_email_result = EmailService.email_validation("test_invalid_email.com")
    assert valid_email_result == True
    assert not valid_email_result == False
    assert invalid_email_result == False
