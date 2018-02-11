from os import environ
from flask import Flask

from routes import setup_routes

default_mysql = 'mysql+mysqldb://root:my-secret-pw@mysql/py_template'


def main():
    app = Flask(__name__, static_url_path='/static')
    app = setup_routes(app)
    sqlalchemy_config = 'SQLALCHEMY_DATABASE_URI'
    app.config[sqlalchemy_config] = environ.get(sqlalchemy_config,
            default_mysql)

    from database import db
    db.init_app(app)

    try:
        db.create_all()
    except:
        print('Database already initialized')

    app.run(host='0.0.0.0', port=environ.get('PORT', 8080))


if __name__ == '__main__':
    main()
