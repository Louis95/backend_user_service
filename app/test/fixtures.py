import pytest

from app.main import create_app


@pytest.fixture
def app():
    return create_app("test")


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    from app.main import db

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()
