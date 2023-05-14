from flaskr.db import get_db
import pickle


def get_state(id):
    if not id or len(id) < 36:
        return None
    db = get_db()
    state = db.execute(
        'SELECT mode, next_section, buffer FROM state where id = ?', [id]).fetchall()
    if len(state) > 0:
        return {'mode': state[0][0], 'next_section': int(state[0][1]), 'buffer': pickle.loads(state[0][2])}
    return None


def initialise_state(id, mode):
    db = get_db()
    next_section = 0
    buffer = pickle.dumps([])
    db.execute('INSERT INTO state VALUES(?, ?, ?, ?)',
               (id, mode, next_section, buffer))
    db.commit()


def update_state(id, state):
    db = get_db()
    buffer = pickle.dumps(state['buffer'])
    db.execute('UPDATE state SET buffer = ?, next_section = ? WHERE id = ?',
               (buffer, state['next_section'], id))
    db.commit()
