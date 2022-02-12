try: 
    from flask_restplus import Api, Resource
except ImportError:
    import werkzeug, flask.scaffold
    werkzeug.cached_property = werkzeug.utils.cached_property
    flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
    from flask_restplus import Api, Resource
from tools.log import setup_custom_logger
import os

api = Api(
    version="0.1",
    title="CIGK API",
    description="This is a REST API for CIGK",
)
logger = setup_custom_logger("api")