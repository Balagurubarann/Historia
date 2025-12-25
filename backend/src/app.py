from flask import Flask
from .extension import db
from src.routes.event_route import event_bp

def create_app():

    app = Flask(__name__)
    app.config.from_object("src.lib.config")

    db.init_app(app)

    app.register_blueprint(event_bp)

    with app.app_context():
        db.create_all()

    return app
