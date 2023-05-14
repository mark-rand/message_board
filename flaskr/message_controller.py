from flask import Blueprint
from flask import jsonify
from flask import current_app
from flask import request
from flaskr.bin_string_utils import columns_to_string
import flaskr.colours as colours
from flaskr import fonts
from flaskr import news_and_weather
from flaskr.db import get_db
import uuid
import json

DEFAULT_CHUNK_SIZE = 120
bp = Blueprint('message_controller', __name__)


@bp.route('/init')
def initialise():
    id = str(uuid.uuid4())
    return_val = jsonify({'id': id})
    mode = request.args.get('mode')
    mode_json = get_mode(mode)
    if mode_json and len(mode_json) > 0:
        from flaskr.state_persistence import initialise_state
        initialise_state(id, mode)
        return return_val
    else:
        return "Unknown mode", 422


@bp.route('/next')
def next():
    uuid = str(request.args.get('id'))
    chunk_count = request.args.get('chunk_count', 1)
    chunk_size = int(request.args.get('chunk_size', DEFAULT_CHUNK_SIZE))
    from flaskr.state_persistence import get_state, update_state
    state = get_state(uuid)
    if not state:
        return "Not found", 404
    chunks = []
    for _ in range(0, chunk_count):
        chunks.append(columns_to_string(get_chunk(chunk_size, state)))
    update_state(uuid, state)
    return jsonify({'chunks': chunks})


def get_chunk(size, state):
    buffer = state['buffer']
    while len(buffer) < size:
        buffer.extend(process_next_section(state))
    chunk = buffer[:size]
    state['buffer'] = buffer[size:]
    return chunk


def process_next_section(this_state):
    buffer = []
    mode_name = this_state['mode']
    modes = get_mode(mode_name)
    section = modes[this_state['next_section'] % len(modes)]
    if section['type'] == 'text':
        font = section['font'] if 'font' in section else 'Px437 Sigma RM 8x8'
        background = section['background'] if 'background' in section else colours.white
        foreground = section['foreground'] if 'foreground' in section else colours.blue
        cols = fonts.append_text(
            section['message'], font, background=background, foreground=foreground)
        buffer.extend(cols)
    elif section['type'] == 'news':
        cols = fonts.append_text(news_and_weather.get_news(
        ), 'Px437 Sigma RM 8x8', foreground=colours.red, background=colours.black)
        buffer.extend(cols)
    elif section['type'] == 'weather':
        location = section['location'] if 'location' in section else '2655642'
        friendly_name = section['friendly_name'] if 'friendly_name' in section else 'Bingley'
        cols = fonts.append_text(news_and_weather.get_weather(
            location, friendly_name), 'Px437 Sigma RM 8x8', foreground=colours.red, background=colours.greyscale)
        buffer.extend(cols)
    elif section['type'] == 'greeting':
        from flaskr.greeting import create_greeting
        if 'timezone' in section:
            buffer.extend(create_greeting(None, timezone=section['timezone']))
        else:
            buffer.extend(create_greeting(None))
    elif section['type'] == 'fixed':
        buffer.extend(section['repeat'])
    else:
        raise ValueError("Invalid mode")
    this_state['next_section'] += 1
    return buffer


def get_mode(mode_name):
    db = get_db()
    parameters = (mode_name,)
    mode = db.execute('SELECT json'
                      ' FROM mode where name = ?',
                      parameters).fetchall()
    if len(mode) > 0:
        print(mode[0][0])
        return json.loads(mode[0][0])
    config = current_app.config['MODES']
    return config[mode_name] if mode_name in config else None
