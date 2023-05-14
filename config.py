import flaskr.colours as colours


class Config(object):
    HEIGHT = 11


class DefaultConfig(Config):
    a = []
    for x in range(224, 32, -32):
        a.append([x]*11)
        a.insert(0, [x]*11)
    MODES = {
        'fixed': [{'type': 'greeting', 'timezone': 'Europe/London'},
                  {'type': 'weather'},
                  {'type': 'fixed',
                   'repeat': [[1] * 11, [2] * 11, [3] * 11, [3] * 11, [3] * 11]},
                  {'type': 'text', 'message': ' Sample config - change this to whatever you like! ', 'font': 'simple_8', 'foreground': [
                      colours.red, colours.orange, colours.yellow, colours.green, colours.indigo, colours.violet], 'background': colours.black},
                  {'type': 'fixed',
                   'repeat': [[3] * 11, [2] * 11, [1] * 11, [1] * 11, [1] * 11]},
                  {'type': 'news'}
                  ],
        'meh': [{'type': 'text', 'message': '!',
                 'font': '1x11', 'background': colours.black}], }
