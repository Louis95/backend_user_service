import unittest

from app.main.models.user import UserModel
from typing import List
from app.test.base import db, app

from flask_sqlalchemy import SQLAlchemy

from app.main.service.user_service import UserService


def save_test_user(db: SQLAlchemy):
    """ The First test does something """
    louis: UserModel = UserModel(first_name="louis", last_name="aso")
    penn: UserModel = UserModel(first_name="penn", last_name="muluh")
    db.session.add(louis)
    db.session.add(penn)
    db.session.commit()


def test_get_all(db: SQLAlchemy):
    """ The First test does something """
    save_test_user(db)
    results: List[UserModel] = UserService.get_all_users()

    assert len(results) == 2
    assert results[0][0]["first_name"] == "louis"
    assert results[0][1]["first_name"] == "penn"


def test_get_user_by_id(db: SQLAlchemy):
    save_test_user(db)
    result = UserService.get_user_by_id(1)

    assert result["first_name"] == "louis"
    assert result["emails"] == []
    assert isinstance(result, dict)


def test_get_user_by_name(db: SQLAlchemy):
    save_test_user(db)
    result = UserService.get_user_by_name("louis")

    assert result["first_name"] == "louis"
    assert result["last_name"] == "aso"


def test_delete_user(db: SQLAlchemy):
    save_test_user(db)
    result = UserService.delete_user(1)

    assert result[0]["message"] == "User Deleted successfully"


def test_save_new_user(db: SQLAlchemy):
    data = {"first_name": "test first name", "last_name": "test last name"}
    result = UserService.save_new_user(data)

    assert result[0]["first_name"] == "test first name"
    assert result[0]["last_name"] == "test last name"
    assert result[1] == 201



