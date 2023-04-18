from flask import current_app
import flaskr.colours as colours
import math


def append_text(text, font_name, foreground=colours.blue, background=colours.white, kerning=1):
    cols = []
    font_def = current_app.config['FONTS'][font_name]
    height = current_app.config['HEIGHT']
    padding_total = height - font_def['height']
    padding_top = [background] * math.ceil(padding_total / 2)
    padding_bottom = [background] * math.floor(padding_total / 2)
    for count, char in enumerate(text):
        this_char_colour = foreground if not isinstance(
            foreground, list) else foreground[count % len(foreground)]
        this_char_background = background if not isinstance(background, list) else background[count % len(background)]
        char_def = font_def['characters'][char] if char in font_def['characters'] else [
            ' ' * font_def['height']] * 3
        for column in char_def:
            this_col = [this_char_colour if pixel ==
                        'o' else background for pixel in column]
            cols.append(padding_top + this_col + padding_bottom)
        if kerning > 0:
            cols.append(*[[background] * height] * kerning)
    return cols
