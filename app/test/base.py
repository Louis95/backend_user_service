import pytest

from app.main import create_app


@pytest.fixture
def app():
    """ The First test does something """
    return create_app("test")


@pytest.fixture
def client(app):
    """ The First test does something """
    return app.test_client()


@pytest.fixture
def db(app):
    """ The First test does something """
    from app.main import db

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()
