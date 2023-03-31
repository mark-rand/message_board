from flask import Blueprint
from flask import jsonify
from flask import current_app
from flask import request
from flaskr import colours
from flaskr import fonts

bp = Blueprint('example_blueprint', __name__)


@bp.route('/')
def index():
    args = request.args
    current_state = int(args.get('state', 0))
    states = current_app.config['STATES']
    current_state = states[current_state % len(states)]
    if current_state['type'] == 'fixed':
        display = {'cols': current_state['cols'],
                   'message': current_state['message']}
        return jsonify(display)
    if current_state['type'] == 'text':
        font = current_state['font'] if 'font' in current_state else '1x11'
        cols=[]
        cols = fonts.append_text(cols, current_state['message'], font)
        display = {'cols': cols, 'message': [1]}
        return jsonify(display)
    return "", 404
