from flask import current_app, redirect, request, jsonify

from database import db, URL
from utils import generate_shortened_url


def index():
    current_app.send_static_file_app.send_static_file('index.html')

def get_url(shortened_url):
    url_entity = URL.query.filter_by(short_url=shortened_url)
    return redirect(url_entity.full_url, 301)

def create_url():
    content = request.get_json()

    full_url = content["url"]
    shortened_url = generate_shortened_url()
    shortened_url_full = '{}{}'.format(request.url_root, shortened_url)

    url = URL(
        full_url=full_url,
        short_url=shortened_url,
        short_url_full=shortened_url_full
    )

    db.session.add(url)
    db.session.commit()

    return jsonify({"url": full_url, "shortened_url": shortened_url_full}), 200


def setup_routes(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/<shortened_url>', 'get_url', get_url)
    app.add_url_rule('/urls', 'create_url', create_url, methods=['POST'])

    return app
