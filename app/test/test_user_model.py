import unittest

from app.main.models.user import UserModel
from pytest import fixture
from app.test.base import db, app


@fixture
def userModel() -> "UserModel":
    """ The First test does something """
    return UserModel(first_name="louis", last_name="test second")


if __name__ == '__main__':
    unittest.main()
