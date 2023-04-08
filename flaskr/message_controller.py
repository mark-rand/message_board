from flask import Blueprint
from flask import jsonify
from flask import current_app
from flask import request
from flaskr.colours import *
from flaskr import fonts
from flaskr import news_and_weather
import uuid

DEFAULT_CHUNK_SIZE = 250
bp = Blueprint('message_controller', __name__)

states = {}


@bp.route('/init')
def initialise():
    id = str(uuid.uuid4())
    mode = request.args.get('mode')
    if not mode in current_app.config['MODES']:
        return "Unknown mode", 422
    states[id] = initialise_state(mode)
    return jsonify({'id': id})


def initialise_state(mode):
    state_data = {'mode': mode, 'next_section': 0, 'buffer': []}
    return state_data


@bp.route('/next')
def next():
    uuid = str(request.args.get('id'))
    chunk_count = request.args.get('chunk_count', 1)
    chunk_size = int(request.args.get('chunk_size', DEFAULT_CHUNK_SIZE))
    if not uuid or len(uuid) < 36:
        return "Invalid UUID", 422
    if uuid not in states:
        return "Not found", 404
    chunks = []
    for _ in range(0, chunk_count):
        chunks.append(get_chunk(uuid, chunk_size))
    return jsonify({'chunks': chunks})


def get_chunk(uuid, size):
    buffer = states[uuid]['buffer']
    while len(buffer) < size:
        buffer.extend(process_next_section(uuid))
    chunk = buffer[:size]
    states[uuid]['buffer'] = buffer[size:]
    return chunk


def process_next_section(uuid):
    buffer = []
    this_state = states[uuid]
    mode_name = this_state['mode']
    modes = current_app.config['MODES'][mode_name]
    section = modes[this_state['next_section'] % len(modes)]
    if section['type'] == 'text':
        font = section['font'] if 'font' in section else 'Px437 Sigma RM 8x8'
        background = section['background'] if 'background' in section else WHITE
        foreground = section['foreground'] if 'foreground' in section else BLUE
        cols = fonts.append_text(
            section['message'], font, background=background, foreground=foreground)
        buffer.extend(cols)
    elif section['type'] == 'news':
        cols = fonts.append_text(news_and_weather.get_news(), 'Px437 Sigma RM 8x8', foreground=RED, background=BLACK)
        buffer.extend(cols)
    elif section['type'] == 'weather':
        location=section['location'] if 'location' in section else '2655642'
        friendly_name=section['friendly_name'] if 'friendly_name' in section else 'Bingley'
        cols = fonts.append_text(news_and_weather.get_weather(location, friendly_name), 'Px437 Sigma RM 8x8', foreground=RED, background=CYAN)
        buffer.extend(cols)
    elif section['type'] == 'fixed':
        buffer.extend(section['repeat'])
    else:
        raise ValueError("Invalid mode")
    this_state['next_section'] += 1
    return buffer
