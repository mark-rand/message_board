from flask import current_app
import flaskr.colours as colours
import math
from flaskr.canvas_array import CanvasArray

ALPHA = -1


def get_bg_for_col(background, column):
    if not isinstance(background, list):
        return background
    return background[column % len(background)]


def get_padding(total_padding, background, column, round_down=False):
    if round_down:
        padding_size = math.floor(total_padding / 2)
    else:
        padding_size = math.ceil(total_padding / 2)
    return [ALPHA] * padding_size


def append_text(text, font_name, foreground=colours.blue, background=colours.white, kerning=1):
    canvas = CanvasArray()
    font_def = current_app.config['FONTS'][font_name]
    height = current_app.config['HEIGHT']
    padding_total = height - font_def['height']
    for count, char in enumerate(text):
        this_char_colour = foreground if not isinstance(
            foreground, list) else foreground[count % len(foreground)]
        char_def = font_def['characters'][char] if char in font_def['characters'] else [
            ' ' * font_def['height']] * 3
        for col_count, column in enumerate(char_def):
            this_col = [this_char_colour if pixel ==
                        'o' else ALPHA for pixel in column]
            canvas.append(get_padding(padding_total, ALPHA, col_count) +
                          this_col + get_padding(padding_total, ALPHA, col_count, True))
        if kerning > 0:
            for k_count in range(kerning):
                canvas.append([ALPHA] * height)
    return canvas.array_with_bg(background)
