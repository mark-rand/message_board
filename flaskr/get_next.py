from flask import Blueprint
from flask import jsonify
from flask import current_app
from flask import request
from flaskr.colours import *
from flaskr import fonts

bp = Blueprint('get_next', __name__)


@bp.route('/')
def index():
    height=current_app.config['HEIGHT']
    args = request.args
    current_state = int(args.get('state', 0))
    states = current_app.config['STATES']
    current_state = states[current_state % len(states)]
    if current_state['type'] == 'fixed':
        display = {'cols': current_state['cols'],
                   'message': current_state['message']}
        return jsonify(display)
    if current_state['type'] == 'text':
        font = current_state['font'] if 'font' in current_state else 'Px437 Sigma RM 8x8'
        background=current_state['background'] if 'background' in current_state else WHITE
        cols=[]
        print(current_state)
        cols = fonts.append_text(cols, current_state['message'], font, background=background)
        display = {'cols': cols, 'message': [1]}
        return jsonify(display)
    elif current_state['type'] == 'ober':
        cols=[]
        for c in range(0,55):
            cols.append(BLUE * height)
            cols.append(RED * height)
        meh = jsonify({'cols':cols})
        return meh
    return "", 404
