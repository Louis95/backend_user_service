import unittest

from app.main import db
from app.main.models.user import User
from app.main.service.user_service import save_new_user
from app.test.base import BaseTestCase


def save_test_user():
    user = User(
        email='test@test.com',
        password='test',
        first_name='test',
        last_name='bleck',
    )
    db.session.add(user)
    db.session.commit()


class TestUserService(BaseTestCase):

    def test_save_new_user(self):
        data = {
            "email": "test@gmail.com",
            "first_name": "test",
            "last_name": "bleck",
            "age": "20",
            "password": "test",
        }

        save_test_user()
        result = save_new_user(data)
        response = {'status': 'success', 'message': 'Successfully created.'}
        self.assertEqual(result[0], response)

    def test_get_a_user(self):
        save_test_user()
        response_object = self.client.get("/user/1")
        self.assertEqual(response_object.status_code, 200)  # 200 = OK
