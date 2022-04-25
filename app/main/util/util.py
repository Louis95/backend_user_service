from flask_seeder import Seeder, Faker, generator
from app.main.models.user import UserModel
from app.main import db

RESULT_PER_PAGE = 100


def paginate_query(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RESULT_PER_PAGE
    end = start + RESULT_PER_PAGE

    items = [item.format() for item in selection]
    current_items = items[start:end]

    return current_items


class SeedUser(Seeder):

    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=UserModel,
            init={
                "email": generator.Email(),
                "first_name": generator.Name(),
                "last_name": generator.Name(),
                "age": generator.Integer(start=15, end=100)
            }
        )

        # Create 5 users
        for user in faker.create(790927):
            print("Adding user: %s" % user)
            db.session.add(user)
            db.session.commit()
