from flask import Flask, Blueprint
from flask_cors import CORS
from api import api, logger
from attendee_namespace import ns as attendee_namespace

app = Flask(__name__)
CORS(app=app)


def initialize_app(flask_app):
    logger.info("Configuring api server")
    blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
    api.init_app(blueprint)
    api.add_namespace(attendee_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    logger.info("Starting api server")
    initialize_app(app)
    app.run(debug="DEBUG")


if __name__ == "__main__":
    main()
