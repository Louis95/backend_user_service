from flask_seeder import Seeder, Faker, generator
from app.main.models.user import UserModel
from app.main.models.email import EmailModel


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
        faker_user = Faker(
            cls=UserModel,
            init={
                "first_name": generator.Name(),
                "last_name": generator.Name(),
            }
        )

        # Create 100 users
        for user in faker_user.create(100):
            print("Adding user: %s" % user)
            db.session.add(user)
            db.session.commit()

        faker_email = Faker(
            cls=EmailModel,
            init={
                "email_address": generator.Email(),
                "user_id": generator.Integer(start=1, end=100),
            }
        )

        # Create 100 emails
        for email in faker_email.create(100):
            print("Adding user: %s" % email)
            db.session.add(email)
            db.session.commit()
