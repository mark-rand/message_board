from flask import current_app
from flaskr.colours import *
import math

def append_text(text, font_name, foreground=BLUE, background=WHITE, kerning=1):
    cols=[]
    font_def=current_app.config['FONTS'][font_name]
    height=current_app.config['HEIGHT']
    padding_total = height - font_def['height']
    padding_top=background * math.ceil(padding_total / 2)
    padding_bottom=background * math.floor(padding_total / 2)
    for count, char in enumerate(text):
        this_char_colour=foreground if not isinstance(foreground, list) else str(foreground[count % len(foreground)])
        char_def = font_def['characters'][char] if char in font_def['characters'] else [' ' * font_def['height']] * 3
        for column in char_def:
            column = column.replace(' ', background).replace('o', this_char_colour)
            cols.append(padding_top + column + padding_bottom)
        if kerning > 0:
            cols.append(''.join([background * height] * kerning))
    return cols