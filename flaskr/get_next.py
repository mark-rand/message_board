from flask import Blueprint
from flask import jsonify
from flask import current_app


bp = Blueprint('example_blueprint', __name__)

@bp.route('/')
def index():
    display=None
    # states = current_app.config['STATES']
    # current_state = states[0]
    # if current_state['type'] == 'text':
    #     display={'type':'text', 'text': current_state['text']}
    cols=[11111111111,22222222222,33333333333]
    message=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]*250
    display={'cols': cols, 'message': message}
    return jsonify(display)