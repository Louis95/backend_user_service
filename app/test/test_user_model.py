import unittest

from app.main import db
from app.main.models.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_format(self):
        user = User(
            email='test@test.com',
            password='test',
            first_name='test',
            last_name='bleck',
        )
        db.session.add(user)
        db.session.commit()
        result = user.format()
        self.assertTrue(result["email"], "test@test.com")
        self.assertTrue(result["first_name"], "test")


if __name__ == '__main__':
    unittest.main()
