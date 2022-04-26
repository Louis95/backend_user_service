from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app
from app.main.models.user import UserModel
from app.main.service.user_service import UserService
from app.main.schemas.user import UserSchema


def make_user(
        first_name: str = "Test first name", last_name: str = "Test last name"
) -> UserModel:
    return UserModel(last_name, first_name)


class TestUsersResource:
    @patch.object(
        UserService,
        "get_all_users",
        lambda: [
            make_user(first_name="Yoh", last_name="Lulu"),
            make_user(first_name="Test Widget 2", last_name="Teng"),
        ],
    )
    def test_get(self, client):

        with client:
            # print(f"client.get("/"))
            results = client.get(f"http://127.0.0.1:5000/user/")
            expected = (
                UserSchema(many=True)
                    .dump(
                    [
                        make_user(first_name="Yoh", last_name="Lulu"),
                        make_user(first_name="Test Widget 2", last_name="Teng"),
                    ]
                )
            )
            print(f"result {results}")
