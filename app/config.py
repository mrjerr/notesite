import os


SQLALCHEMY_TRACK_MODIFICATIONS = False


WTF_CSRF_ENABLED = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key-only-for-testing'

DB_HOST = os.environ.get('DB_HOST', False)
DB_PASS = os.environ.get('DB_PASS', False)
DB_NAME = os.environ.get('DB_NAME', False)
DB_USER = os.environ.get('DB_USER', False)

SQLALCHEMY_DATABASE_URI = (
    "mysql://{db_user}:{db_pass}@{db_host}/{db_name}".format(
            db_user=DB_USER, db_pass=DB_PASS, db_host=DB_HOST, db_name=DB_NAME
        )
    if all([DB_HOST, DB_PASS, DB_NAME, DB_USER])
    else 'sqlite:///' + os.path.join(BASE_DIR, 'app.sqlite')
)
