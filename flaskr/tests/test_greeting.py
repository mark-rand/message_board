from flaskr.greeting import get_day_segment, TimeOfDay, create_greeting, ordinal_suffix
from unittest.mock import patch
from datetime import datetime
from zoneinfo import ZoneInfo


def test_greetings():
    time_tuple = datetime(2022, 12, 28, 8, 44, 4, 4)
    assert get_day_segment(time_tuple) == TimeOfDay.MORNING
    time_tuple = datetime(2022, 12, 28, 23, 44, 4, 4)
    assert get_day_segment(time_tuple) == TimeOfDay.EVENING
    time_tuple = datetime(2022, 12, 28, 11, 59, 4, 4)
    assert get_day_segment(time_tuple) == TimeOfDay.MORNING
    time_tuple = datetime(2022, 12, 28, 0, 0, 4, 4)
    assert get_day_segment(time_tuple) == TimeOfDay.MORNING
    time_tuple = datetime(2022, 12, 28, 23, 59, 59, 4)
    assert get_day_segment(time_tuple) == TimeOfDay.EVENING
    time_tuple = datetime(2022, 12, 28, 12, 59, 59, 4)
    assert get_day_segment(time_tuple) == TimeOfDay.AFTERNOON


@patch('flaskr.greeting.append_text')
def test_create_greeting(test_patch):
    time_tuple = datetime(2022, 1, 2, 11, 59, 59, 4)
    create_greeting(time_tuple)
    test_patch.assert_called_with(' Good morning, it is 11:59 on 2nd January ', 'CG Pixel 4x5', background=1, foreground=237)
    time_tuple = datetime(2022, 1, 1, 11, 59, 59, 4)
    create_greeting(time_tuple)
    test_patch.assert_called_with(' Happy New Year! It is 11:59 on 1st January ', 'CG Pixel 4x5', background=1, foreground=237)
    time_tuple = datetime(2022, 12, 28, 16, 59, 59, 4)
    create_greeting(time_tuple)
    test_patch.assert_called_with(' Good afternoon, it is 16:59 on 28th December ', 'CG Pixel 4x5', background=1, foreground=237)
    time_tuple = datetime(2022, 1, 3, 16, 59, 59, 4, tzinfo=ZoneInfo('Europe/Berlin'))
    create_greeting(time_tuple)
    test_patch.assert_called_with(' Good afternoon, it is 16:59 on 3rd January ', 'CG Pixel 4x5', background=1, foreground=237)
    create_greeting(time_tuple, "Europe/London")
    test_patch.assert_called_with(' Good afternoon, it is 15:59 on 3rd January ', 'CG Pixel 4x5', background=1, foreground=237)


def test_ordinal_suffix():
    assert ordinal_suffix(1) == 'st'
    assert ordinal_suffix(2) == 'nd'
    assert ordinal_suffix(12) == 'th'
    assert ordinal_suffix(3) == 'rd'
    assert ordinal_suffix(13) == 'th'
