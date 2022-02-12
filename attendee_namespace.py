try: 
    from flask_restplus import fields, Resource
except ImportError:
    import werkzeug, flask.scaffold
    werkzeug.cached_property = werkzeug.utils.cached_property
    flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
    from flask_restplus import fields, Resource

from api import api, logger

ns = api.namespace(
    "resources/attendees",
    description="Operations related to attendees checking",
)

kanban_model = api.model(
    "Attendee Model",
    {
        "name": fields.String(required=True, description="Ateendee name"),
        "surname": fields.String(required=True, description="Ateendee surname"),
    },
)

@ns.route("/")
class AttendeesAll(Resource):
    """ Endpoints for Attendees """

    @api.response(200, "Attendees fetched")
    @api.response(500, "Could not fetch Attendees info")
    def get(self):
        """Returns all kanban boards with info"""
        logger.info("Fetching all attendees info")
        return "Attendee"