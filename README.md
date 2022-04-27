
## User service
![user service endpoints](userservice_enpoints.png)

user rest-service for:
 - Creating a new user with contact data
 - Get user by Id and name
 - Add email/phone number
 - Update existing mail/phone data
 - Delete user
 
 
 ## Running the project
 Preferably, first create a virtualenv and activate it, perhaps with the following command:

```
virtualenv -p python3 venv
source venv/bin/activate
```

Next, run
```
pip install -r requirements.txt
```

Next, run the database migrations

```
> python manage.py db init

> python manage.py db migrate --message 'initial database migration'

> python manage.py db upgrade
```
finally type
```python manage.py run``` to run the project

### Endpoints

You can import collection.json into postman to test the different endpoints

### Running Tests
To run the test suite, simply pip install it and run from the root directory like so

```
pip install pytest
pytest
```