from flask import Flask

from views import setup_views


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from model import db
    db.init_app(app)

    setup_views(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.config['DEBUG'] = True

    app.run()
