from flask import Blueprint
import uuid

bp = Blueprint('get_uuid', __name__)


@bp.route('/uuid')
def index():
    return str(uuid.uuid4())
