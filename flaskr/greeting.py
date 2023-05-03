from datetime import datetime
from enum import Enum
from flaskr.fonts import append_text
import flaskr.colours as colours
from zoneinfo import ZoneInfo


class TimeOfDay(Enum):
    MORNING = 0,
    AFTERNOON = 1,
    EVENING = 2


greetings = {TimeOfDay.MORNING: 'morning',
             TimeOfDay.AFTERNOON: 'afternoon', TimeOfDay.EVENING: 'evening'}


def get_day_segment(now):
    hour = int(now.strftime('%H'))

    if (hour >= 0 and hour < 12):
        return TimeOfDay.MORNING
    elif (hour >= 12 and hour < 17):
        return TimeOfDay.AFTERNOON
    else:
        return TimeOfDay.EVENING


def create_greeting(now, timezone=None):
    if not now:
        now = datetime.now()
    if timezone:
        now = now.astimezone(ZoneInfo(timezone))
    time_of_day = get_day_segment(now)
    time_str = now.strftime('%H:%M')
    day_of_month = str(int(now.strftime('%d')))
    day_str = f'{day_of_month}{ordinal_suffix(int(day_of_month))}'
    greeting = f'Good {greetings[time_of_day]}, it is {time_str} on {day_str} {now.strftime("%B")}'
    return append_text(greeting, 'CG Pixel 4x5', background=1, foreground=colours.coral)


def ordinal_suffix(day: int) -> str:
    return {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th') if day not in (11, 12, 13) else 'th'
