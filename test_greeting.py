from flaskr.greeting import get_day_segment, TimeOfDay, create_greeting, ordinal_suffix
from unittest.mock import patch


def test_greetings():
    time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
    assert get_day_segment(time_tuple) == TimeOfDay.MORNING
    time_tuple = (2022, 12, 28, 23, 44, 4, 4, 362, 0)
    assert get_day_segment(time_tuple) == TimeOfDay.EVENING
    time_tuple = (2022, 12, 28, 11, 59, 4, 4, 362, 0)
    assert get_day_segment(time_tuple) == TimeOfDay.MORNING
    time_tuple = (2022, 12, 28, 0, 0, 4, 4, 362, 0)
    assert get_day_segment(time_tuple) == TimeOfDay.MORNING
    time_tuple = (2022, 12, 28, 23, 59, 59, 4, 362, 0)
    assert get_day_segment(time_tuple) == TimeOfDay.EVENING
    time_tuple = (2022, 12, 28, 12, 59, 59, 4, 362, 0)
    assert get_day_segment(time_tuple) == TimeOfDay.AFTERNOON


@patch('flaskr.greeting.append_text')
def test_create_greeting(test_patch):
    time_tuple = (2022, 12, 28, 16, 59, 59, 4, 362, 0)
    create_greeting(time_tuple)
    test_patch.assert_called_with('Good afternoon, it is 16:59 on 28th December', 'CG Pixel 4x5', background=1, foreground=237)


def test_ordinal_suffix():
    assert ordinal_suffix(1) == 'st'
    assert ordinal_suffix(2) == 'nd'
    assert ordinal_suffix(12) == 'th'
    assert ordinal_suffix(3) == 'rd'
    assert ordinal_suffix(13) == 'th'
