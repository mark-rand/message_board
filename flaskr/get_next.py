from flask import Blueprint
from flask import jsonify

bp = Blueprint('example_blueprint', __name__)

@bp.route('/')
def index():
    display={'hello':'world'}
    return jsonify(display)