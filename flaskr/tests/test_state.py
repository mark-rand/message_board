from flaskr.state_persistence import initialise_state, get_state, update_state


def test_state(db_app):
    with db_app.app_context():
        id = 'i' * 36
        state = get_state('non-existent-state')
        assert not state
        initialise_state(id, 'mode')
        state = get_state(id)
        assert state['buffer'] == []
        assert state['next_section'] == 0
        state['buffer'] = ['meh']
        state['next_section'] = + 1
        update_state(id, state)
        state = get_state(id)
        assert state['buffer'] == ['meh']
        assert state['next_section'] == 1
