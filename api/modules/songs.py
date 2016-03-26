from flask import Blueprint

from api.lib.helpers import jsonify

blueprint = Blueprint('songs', __name__)


@blueprint.route('/songs/search/')
def search():
    pass
