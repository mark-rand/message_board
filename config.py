import flaskr.colours as colours


class Config(object):
    HEIGHT = 11
    FONTS = {
        "simple_8": {
            "name": "simple_8",
            "height": 8,
            "characters": {
                "!": [
                    "ooooo o "
                ],
                "\"": [
                    "o       ",
                    " oo     ",
                    "   oo   ",
                    "     oo "
                ],
                "#": [
                    "   o o  ",
                    "  ooooo ",
                    "   o o  ",
                    "  ooooo ",
                    "   o o  "
                ],
                "$": [
                    "  o  o  ",
                    " o oooo ",
                    "oooo o  ",
                    " o  o   "
                ],
                "%": [
                    " oo  oo ",
                    "    o   ",
                    "   o    ",
                    " oo  oo "
                ],
                "&": [
                    " oo oo  ",
                    "o  o  o ",
                    "o  o  o ",
                    "  ooooo "
                ],
                "'": [
                    "oo      "
                ],
                "(": [
                    "  ooo   ",
                    " o   o  ",
                    "o     o "
                ],
                ")": [
                    "o     o ",
                    " o   o  ",
                    "  ooo   "
                ],
                "*": [
                    "  o o o ",
                    "   ooo  ",
                    "  o o o "
                ],
                "+": [
                    "    o   ",
                    "   ooo  ",
                    "    o   "
                ],
                ",": [
                    "       o",
                    "     oo "
                ],
                "-": [
                    "    o   ",
                    "    o   ",
                    "    o   "
                ],
                ".": [
                    "     oo ",
                    "     oo "
                ],
                "/": [
                    "     oo ",
                    "   oo   ",
                    " oo     ",
                    "o       "
                ],
                "0": [
                    " ooooo  ",
                    "o     o ",
                    "o     o ",
                    " ooooo  "
                ],
                "1": [
                    " o    o ",
                    "ooooooo ",
                    "      o "
                ],
                "2": [
                    " o   oo ",
                    "o   o o ",
                    "o  o  o ",
                    " oo   o "
                ],
                "3": [
                    "o    o  ",
                    "o  o  o ",
                    "o oo  o ",
                    "oo  oo  "
                ],
                "4": [
                    "   oo   ",
                    " oo o   ",
                    "o   o   ",
                    "ooooooo "
                ],
                "5": [
                    "oooo  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "o   oo  "
                ],
                "6": [
                    "  oooo  ",
                    " o o  o ",
                    "o  o  o ",
                    "    oo  "
                ],
                "7": [
                    "o       ",
                    "o    oo ",
                    "o  oo   ",
                    "ooo     "
                ],
                "8": [
                    " oo oo  ",
                    "o  o  o ",
                    "o  o  o ",
                    " oo oo  "
                ],
                "9": [
                    " oo     ",
                    "o  o  o ",
                    "o  o o  ",
                    " oooo   "
                ],
                ":": [
                    "oo  oo  "
                ],
                ";": [
                    "       o",
                    "  oo oo "
                ],
                "<": [
                    "    o   ",
                    "   o o  ",
                    "  o   o "
                ],
                "=": [
                    "   o o  ",
                    "   o o  ",
                    "   o o  "
                ],
                ">": [
                    "  o   o ",
                    "   o o  ",
                    "    o   "
                ],
                "?": [
                    " o      ",
                    "o   o o ",
                    "o  o    ",
                    " oo     "
                ],
                "@": [
                    " ooooo  ",
                    "o  o  o ",
                    "o o o o ",
                    " oooo o "
                ],
                "A": [
                    " oooooo ",
                    "o  o    ",
                    "o  o    ",
                    " oooooo "
                ],
                "B": [
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    " oo oo  "
                ],
                "C": [
                    " ooooo  ",
                    "o     o ",
                    "o     o ",
                    " o   o  "
                ],
                "D": [
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    " ooooo  "
                ],
                "E": [
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o     o "
                ],
                "F": [
                    "ooooooo ",
                    "o  o    ",
                    "o  o    ",
                    "o       "
                ],
                "G": [
                    " ooooo  ",
                    "o     o ",
                    "o  o  o ",
                    "o  oooo "
                ],
                "H": [
                    "ooooooo ",
                    "   o    ",
                    "   o    ",
                    "ooooooo "
                ],
                "I": [
                    "o     o ",
                    "ooooooo ",
                    "o     o "
                ],
                "J": [
                    "    oo  ",
                    "      o ",
                    "      o ",
                    "oooooo  "
                ],
                "K": [
                    "ooooooo ",
                    "   o    ",
                    "  o o   ",
                    "oo   oo "
                ],
                "L": [
                    "ooooooo ",
                    "      o ",
                    "      o ",
                    "      o "
                ],
                "M": [
                    "ooooooo ",
                    " o      ",
                    "  o     ",
                    " o      ",
                    "ooooooo "
                ],
                "N": [
                    "ooooooo ",
                    " o      ",
                    "  o     ",
                    "ooooooo "
                ],
                "O": [
                    " ooooo  ",
                    "o     o ",
                    "o     o ",
                    " ooooo  "
                ],
                "P": [
                    "ooooooo ",
                    "o  o    ",
                    "o  o    ",
                    " oo     "
                ],
                "Q": [
                    " ooooo  ",
                    "o     o ",
                    "o    o  ",
                    " oooo o "
                ],
                "R": [
                    "ooooooo ",
                    "o  o    ",
                    "o  oo   ",
                    " oo  oo "
                ],
                "S": [
                    " oo   o ",
                    "o  o  o ",
                    "o  o  o ",
                    "o   oo  "
                ],
                "T": [
                    "o       ",
                    "o       ",
                    "ooooooo ",
                    "o       ",
                    "o       "
                ],
                "U": [
                    "oooooo  ",
                    "      o ",
                    "      o ",
                    "oooooo  "
                ],
                "V": [
                    "ooooooo ",
                    "      o ",
                    "     o  ",
                    "ooooo   "
                ],
                "W": [
                    "oooooo  ",
                    "      o ",
                    "     o  ",
                    "      o ",
                    "oooooo  "
                ],
                "X": [
                    "ooo ooo ",
                    "   o    ",
                    "   o    ",
                    "ooo ooo "
                ],
                "Y": [
                    "ooo   o ",
                    "   o  o ",
                    "   o  o ",
                    "oooooo  "
                ],
                "Z": [
                    "o   ooo ",
                    "o  o  o ",
                    "o o   o ",
                    "oo    o "
                ],
                "[": [
                    "ooooooo ",
                    "o     o "
                ],
                "]": [
                    "o     o ",
                    "ooooooo "
                ],
                "^": [
                    "  o     ",
                    " o      ",
                    "  o     "
                ],
                "_": [
                    "      o ",
                    "      o ",
                    "      o "
                ],
                "`": [
                    "o       ",
                    "o       "
                ],
                "a": [
                    "     o  ",
                    "  o o o ",
                    "  o o o ",
                    "   oooo "
                ],
                "b": [
                    "ooooooo ",
                    "  o   o ",
                    "  o   o ",
                    "   ooo  "
                ],
                "c": [
                    "   ooo  ",
                    "  o   o ",
                    "  o   o ",
                    "   o o  "
                ],
                "d": [
                    "   ooo  ",
                    "  o   o ",
                    "  o   o ",
                    "ooooooo "
                ],
                "e": [
                    "   ooo  ",
                    "  o o o ",
                    "  o o o ",
                    "   oo o "
                ],
                "f": [
                    " oooooo ",
                    "o  o    ",
                    "o  o    ",
                    " o      "
                ],
                "g": [
                    "   oo   ",
                    "  o  o o",
                    "  o  o o",
                    "  ooooo "
                ],
                "h": [
                    "ooooooo ",
                    "  o     ",
                    "  o     ",
                    "   oooo "
                ],
                "i": [
                    "  o     ",
                    "o ooooo ",
                    "      o "
                ],
                "j": [
                    "     oo ",
                    "       o",
                    "       o",
                    "o ooooo "
                ],
                "k": [
                    "ooooooo ",
                    "    o   ",
                    "   o o  ",
                    "  o   o "
                ],
                "l": [
                    "o       ",
                    "ooooooo ",
                    "      o "
                ],
                "m": [
                    "  ooooo ",
                    "  o     ",
                    "   oooo ",
                    "  o     ",
                    "   oooo "
                ],
                "n": [
                    "  ooooo ",
                    "  o     ",
                    "  o     ",
                    "   oooo "
                ],
                "o": [
                    "   ooo  ",
                    "  o   o ",
                    "  o   o ",
                    "   ooo  "
                ],
                "p": [
                    "  oooooo",
                    "  o  o  ",
                    "  o  o  ",
                    "   oo   "
                ],
                "q": [
                    "   oo   ",
                    "  o  o  ",
                    "  o  o  ",
                    "  oooooo"
                ],
                "r": [
                    "  ooooo ",
                    "   o    ",
                    "  o     ",
                    "  o     "
                ],
                "s": [
                    "   o  o ",
                    "  o o o ",
                    "  o o o ",
                    "  o  o  "
                ],
                "t": [
                    " ooooo  ",
                    "  o   o ",
                    "  o   o ",
                    "     o  "
                ],
                "u": [
                    "  oooo  ",
                    "      o ",
                    "      o ",
                    "  ooooo "
                ],
                "v": [
                    "  ooooo ",
                    "      o ",
                    "     o  ",
                    "  ooo   "
                ],
                "w": [
                    "  oooo  ",
                    "      o ",
                    "     o  ",
                    "      o ",
                    "  oooo  "
                ],
                "x": [
                    "  oo oo ",
                    "    o   ",
                    "    o   ",
                    "  oo oo "
                ],
                "y": [
                    "  ooo   ",
                    "     o o",
                    "     o o",
                    "  ooooo "
                ],
                "z": [
                    "  o  oo ",
                    "  o o o ",
                    "  oo  o "
                ],
                "{": [
                    "   o    ",
                    " ooooo  ",
                    "o     o "
                ],
                "|": [
                    "ooooooo "
                ],
                "}": [
                    "o     o ",
                    " ooooo  ",
                    "   o    "
                ],
                "~": [
                    "   o    ",
                    "  o     ",
                    "   o    ",
                    "  o     "
                ],
                "Æ": [
                    " oooooo ",
                    "o  o    ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o "
                ],
                "Þ": [
                    " oooooo ",
                    "  o  o  ",
                    "  o  o  ",
                    "   oo   "
                ],
                "ß": [
                    " oooooo ",
                    "o  o    ",
                    "o  o  o ",
                    " oo oo  "
                ],
                "æ": [
                    "     o  ",
                    "  o o o ",
                    "   oooo ",
                    "  o o o ",
                    "   oo o "
                ],
                "þ": [
                    "ooooooo ",
                    "  o  o  ",
                    "  o  o  ",
                    "   oo   "
                ],
                "£": [
                    "   o    ",
                    " oooooo ",
                    "o  o  o ",
                    "o     o "
                ],
                "¥": [
                    "ooo   o ",
                    "   o  o ",
                    "   o  o ",
                    "oooooo  "
                ],
                "©": [
                    "   ooo  ",
                    "  o   o ",
                    "  o   o ",
                    "   o o  "
                ],
                "°": [
                    " o      ",
                    "o o     ",
                    " o      "
                ]
            }
        },
        "simple_6": {
            "name": "simple_6",
            "height": 6,
            "characters": {
                "!": [
                    " ooo o"
                ],
                "\"": [
                    " o    ",
                    "  oo  ",
                    "    oo"
                ],
                "#": [
                    "  o o ",
                    " ooooo",
                    "  o o ",
                    " ooooo",
                    "  o o "
                ],
                "$": [
                    "  o   ",
                    " o o o",
                    " ooooo",
                    " o o o",
                    "    o "
                ],
                "%": [
                    " o   o",
                    "    o ",
                    "   o  ",
                    "  o   ",
                    " o   o"
                ],
                "&": [
                    "  o o ",
                    " o o o",
                    " o o o",
                    "  oo o",
                    "    o ",
                    "   o o"
                ],
                "'": [
                    " oo   "
                ],
                "(": [
                    "  ooo ",
                    " o   o"
                ],
                ")": [
                    " o   o",
                    "  ooo "
                ],
                "*": [
                    "  o o ",
                    "   o  ",
                    "  o o "
                ],
                "+": [
                    "   o  ",
                    "  ooo ",
                    "   o  "
                ],
                ",": [
                    "     oo "
                ],
                "-": [
                    "   o  ",
                    "   o  ",
                    "   o  "
                ],
                ".": [
                    "     o"
                ],
                "/": [
                    "    oo",
                    "  oo  ",
                    " o    "
                ],
                "0": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   o",
                    " oooo "
                ],
                "1": [
                    " o    ",
                    " ooooo"
                ],
                "2": [
                    " o  oo",
                    " o o o",
                    " o o o",
                    "  o  o"
                ],
                "3": [
                    " o o o",
                    " o o o",
                    " o o o",
                    " oo o "
                ],
                "4": [
                    " ooo  ",
                    "    o ",
                    "    o ",
                    " ooooo",
                    "    o "
                ],
                "5": [
                    " ooo o",
                    " o o o",
                    " o o o",
                    " o  o "
                ],
                "6": [
                    "  oooo",
                    " o o o",
                    " o o o",
                    " o o o",
                    " o  o "
                ],
                "7": [
                    " oo   ",
                    " o    ",
                    " o   o",
                    " o  o ",
                    " ooo  "
                ],
                "8": [
                    "  o o ",
                    " o o o",
                    " o o o",
                    " o o o",
                    " oo o "
                ],
                "9": [
                    "  o   ",
                    " o o o",
                    " o o o",
                    " o o o",
                    " oooo "
                ],
                ":": [
                    "  o  o"
                ],
                ";": [
                    "  o  oo "
                ],
                "<": [
                    "   o  ",
                    "  o o ",
                    " o   o"
                ],
                "=": [
                    "  o o ",
                    "  o o ",
                    "  o o "
                ],
                ">": [
                    " o   o",
                    "  o o ",
                    "   o  "
                ],
                "?": [
                    " o    ",
                    " o o o",
                    " o o  ",
                    "  o   "
                ],
                "@": [
                    "  oooo",
                    " o    ",
                    " o oo ",
                    " o o o",
                    " o   o",
                    " oooo "
                ],
                "A": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  o ",
                    " ooooo"
                ],
                "B": [
                    "  oooo",
                    " o o o",
                    " o o o",
                    " ooo o",
                    "    o "
                ],
                "C": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   o"
                ],
                "D": [
                    "  oooo",
                    " o   o",
                    " o   o",
                    " o   o",
                    "  ooo "
                ],
                "E": [
                    "  oooo",
                    " o o o",
                    " o o o",
                    " o o o"
                ],
                "F": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  o "
                ],
                "G": [
                    "  oooo",
                    " o   o",
                    " o   o",
                    " o o o",
                    " o oo "
                ],
                "H": [
                    " ooooo",
                    "   o  ",
                    "   o  ",
                    " ooooo"
                ],
                "I": [
                    " o   o",
                    " ooooo",
                    " o   o"
                ],
                "J": [
                    "    oo",
                    " o   o",
                    " o   o",
                    " oooo "
                ],
                "K": [
                    " ooooo",
                    "   o  ",
                    "  oo  ",
                    " o  oo"
                ],
                "L": [
                    " ooooo",
                    "     o",
                    "     o",
                    "     o"
                ],
                "M": [
                    "  oooo",
                    " o    ",
                    "  oooo",
                    " o    ",
                    "  oooo"
                ],
                "N": [
                    "  oooo",
                    " o    ",
                    " o    ",
                    " o    ",
                    " ooooo"
                ],
                "O": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   o",
                    " oooo "
                ],
                "P": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  o ",
                    " ooo  "
                ],
                "Q": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   oo ",
                    " oooo "
                ],
                "R": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  oo",
                    " ooo  "
                ],
                "S": [
                    "  o  o",
                    " o o o",
                    " o o o",
                    " o  o "
                ],
                "T": [
                    " o    ",
                    " o    ",
                    " ooooo",
                    " o    ",
                    " o    "
                ],
                "U": [
                    " oooo ",
                    "     o",
                    "     o",
                    "     o",
                    " oooo "
                ],
                "V": [
                    " ooo  ",
                    "    o ",
                    "     o",
                    "    o ",
                    " ooo  "
                ],
                "W": [
                    " ooooo",
                    "     o",
                    " oooo ",
                    "     o",
                    " oooo "
                ],
                "X": [
                    " oo oo",
                    "   o  ",
                    "   o  ",
                    " oo oo"
                ],
                "Y": [
                    " oo  o",
                    "   o o",
                    "   o o",
                    " oooo "
                ],
                "Z": [
                    " o  oo",
                    " o o o",
                    " o o o",
                    " oo  o"
                ],
                "[": [
                    " ooooo",
                    " o   o"
                ],
                "]": [
                    " o   o",
                    " ooooo"
                ],
                "^": [
                    "  o   ",
                    " o    ",
                    "  o   "
                ],
                "_": [
                    "     o",
                    "     o",
                    "     o"
                ],
                "`": [
                    " o    ",
                    "  o   "
                ],
                "a": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  o ",
                    " ooooo"
                ],
                "b": [
                    "  oooo",
                    " o o o",
                    " o o o",
                    " ooo o",
                    "    o "
                ],
                "c": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   o"
                ],
                "d": [
                    "  oooo",
                    " o   o",
                    " o   o",
                    " o   o",
                    "  ooo "
                ],
                "e": [
                    "  oooo",
                    " o o o",
                    " o o o",
                    " o o o"
                ],
                "f": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  o "
                ],
                "g": [
                    "  oooo",
                    " o   o",
                    " o   o",
                    " o o o",
                    " o oo "
                ],
                "h": [
                    " ooooo",
                    "   o  ",
                    "   o  ",
                    " ooooo"
                ],
                "i": [
                    " o   o",
                    " ooooo",
                    " o   o"
                ],
                "j": [
                    "    oo",
                    " o   o",
                    " o   o",
                    " oooo "
                ],
                "k": [
                    " ooooo",
                    "   o  ",
                    "  oo  ",
                    " o  oo"
                ],
                "l": [
                    " ooooo",
                    "     o",
                    "     o",
                    "     o"
                ],
                "m": [
                    "  oooo",
                    " o    ",
                    "  oooo",
                    " o    ",
                    " ooooo"
                ],
                "n": [
                    "  oooo",
                    " o    ",
                    " o    ",
                    " o    ",
                    " ooooo"
                ],
                "o": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   o",
                    " oooo "
                ],
                "p": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  o ",
                    " ooo  "
                ],
                "q": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   oo ",
                    " oooo "
                ],
                "r": [
                    "  oooo",
                    " o  o ",
                    " o  o ",
                    " o  oo",
                    " ooo  "
                ],
                "s": [
                    " oo  o",
                    "   o o",
                    "   o o",
                    " oooo "
                ],
                "t": [
                    " o    ",
                    " o    ",
                    " ooooo",
                    " o    ",
                    " o    "
                ],
                "u": [
                    " oooo ",
                    "     o",
                    "     o",
                    "     o",
                    " oooo "
                ],
                "v": [
                    " ooo  ",
                    "    o ",
                    "     o",
                    "    o ",
                    " ooo  "
                ],
                "w": [
                    " ooooo",
                    "     o",
                    " oooo ",
                    "     o",
                    " oooo "
                ],
                "x": [
                    " oo oo",
                    "   o  ",
                    "   o  ",
                    " oo oo"
                ],
                "y": [
                    " oo  o",
                    "   o o",
                    "   o o",
                    " oooo "
                ],
                "z": [
                    " o  oo",
                    " o o o",
                    " o o o",
                    " oo  o"
                ],
                "{": [
                    "   o  ",
                    " ooooo",
                    " o   o"
                ],
                "|": [
                    " ooooo"
                ],
                "}": [
                    " o   o",
                    " ooooo",
                    "   o  "
                ],
                "~": [
                    "  o   ",
                    " o    ",
                    " o    "
                ],
                "Æ": [
                    "  oooo",
                    " o  o ",
                    "  oooo",
                    " o o o",
                    " o o o"
                ],
                "Þ": [
                    "oooooo",
                    " o  o ",
                    " o  o ",
                    " o  o ",
                    " ooo  "
                ],
                "ß": [
                    " ooooo",
                    " o o  ",
                    " o o o",
                    "  o oo"
                ],
                "æ": [
                    "  oooo",
                    " o  o ",
                    "  oooo",
                    " o o o",
                    " o o o"
                ],
                "þ": [
                    "oooooo",
                    " o  o ",
                    " o  o ",
                    " o  o ",
                    " ooo  "
                ],
                "£": [
                    "   o  ",
                    "  oooo",
                    " o o o",
                    " o o o"
                ],
                "©": [
                    "  ooo ",
                    " o   o",
                    " o   o",
                    " o   o"
                ],
                "°": [
                    " o    ",
                    "o o   ",
                    " o    "
                ]
            }
        },

        "Px437 Sigma RM 8x8": {
            "name": "Px437 Sigma RM 8x8",
            "height": 8,
            "characters": {
                "°": [
                    " oo     ",
                    " oo     ",
                ],
                "!": [
                    " oo     ",
                    "ooooo o ",
                    "ooooo o ",
                    " oo     "
                ],
                "\"": [
                    "o       ",
                    "ooo     ",
                    "        ",
                    "o       ",
                    "ooo     "
                ],
                "#": [
                    "  o o   ",
                    "ooooooo ",
                    "ooooooo ",
                    "  o o   ",
                    "ooooooo ",
                    "ooooooo ",
                    "  o o   "
                ],
                "$": [
                    "  o  o  ",
                    " ooo o  ",
                    " o o o  ",
                    "ooooooo ",
                    " o o o  ",
                    " o ooo  ",
                    "    o   "
                ],
                "%": [
                    "  oo  o ",
                    " o o oo ",
                    " oo oo  ",
                    "   oo   ",
                    "  oo oo ",
                    " oo o o ",
                    " o  oo  "
                ],
                "&": [
                    "    oo  ",
                    " o oooo ",
                    "o oo  o ",
                    "o oo  o ",
                    "ooooooo ",
                    " o  oo  ",
                    "    o o "
                ],
                "'": [
                    "o o     ",
                    "oo      "
                ],
                "(": [
                    "  ooo   ",
                    " ooooo  ",
                    "oo   oo ",
                    "o     o "
                ],
                ")": [
                    "o     o ",
                    "oo   oo ",
                    " ooooo  ",
                    "  ooo   "
                ],
                "*": [
                    "   o    ",
                    " o o o  ",
                    " ooooo  ",
                    "  ooo   ",
                    "  ooo   ",
                    " ooooo  ",
                    " o o o  ",
                    "   o    "
                ],
                "+": [
                    "   o    ",
                    "   o    ",
                    " ooooo  ",
                    " ooooo  ",
                    "   o    ",
                    "   o    "
                ],
                ",": [
                    "     o o",
                    "     oo "
                ],
                "-": [
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    "
                ],
                ".": [
                    "      o ",
                    "      o "
                ],
                "/": [
                    "      o ",
                    "     oo ",
                    "    oo  ",
                    "   oo   ",
                    "  oo    ",
                    " oo     ",
                    "oo      "
                ],
                "0": [
                    " ooooo  ",
                    "ooooooo ",
                    "o   ooo ",
                    "o  oo o ",
                    "o oo  o ",
                    "ooooooo ",
                    " ooooo  "
                ],
                "1": [
                    "  o   o ",
                    " oo   o ",
                    "ooooooo ",
                    "ooooooo ",
                    "      o ",
                    "      o "
                ],
                "2": [
                    " o   oo ",
                    "oo  ooo ",
                    "o   o o ",
                    "o  oo o ",
                    "o  o  o ",
                    "oooo  o ",
                    " oo   o "
                ],
                "3": [
                    " o   o  ",
                    "oo   oo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " oo oo  "
                ],
                "4": [
                    "   oo   ",
                    "  ooo   ",
                    " oo o   ",
                    "oo  o o ",
                    "ooooooo ",
                    "ooooooo ",
                    "    o o "
                ],
                "5": [
                    "ooo  o  ",
                    "ooo  oo ",
                    "o o   o ",
                    "o o   o ",
                    "o o   o ",
                    "o ooooo ",
                    "o  ooo  "
                ],
                "6": [
                    " ooooo  ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "oo oooo ",
                    " o  oo  "
                ],
                "7": [
                    "ooo     ",
                    "oo      ",
                    "o    oo ",
                    "o   ooo ",
                    "o  oo   ",
                    "oooo    ",
                    "ooo     "
                ],
                "8": [
                    " oo oo  ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " oo oo  "
                ],
                "9": [
                    " oo  o  ",
                    "oooo oo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " ooooo  "
                ],
                ":": [
                    " o   o  ",
                    " o   o  "
                ],
                ";": [
                    " o   o o",
                    " o   oo "
                ],
                "<": [
                    "   o    ",
                    "  ooo   ",
                    " oo oo  ",
                    "oo   oo ",
                    "o     o "
                ],
                "=": [
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  "
                ],
                ">": [
                    "o     o ",
                    "oo   oo ",
                    " oo oo  ",
                    "  ooo   ",
                    "   o    "
                ],
                "?": [
                    " o      ",
                    "oo      ",
                    "o   o o ",
                    "o  oo o ",
                    "oooo    ",
                    " oo     "
                ],
                "@": [
                    " ooooo  ",
                    "o     o ",
                    "o  o  o ",
                    "o o o o ",
                    "o o o o ",
                    "o ooo o ",
                    " oooo   "
                ],
                "A": [
                    " oooooo ",
                    "ooooooo ",
                    "o  o    ",
                    "o  o    ",
                    "o  o    ",
                    "ooooooo ",
                    " oooooo "
                ],
                "B": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " oo oo  "
                ],
                "C": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "o     o ",
                    "oo   oo ",
                    " o   o  "
                ],
                "D": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "ooooooo ",
                    " ooooo  "
                ],
                "E": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "o ooo o ",
                    "o     o ",
                    "oo   oo "
                ],
                "F": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "o ooo   ",
                    "o       ",
                    "oo      "
                ],
                "G": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "o   o o ",
                    "ooo ooo ",
                    " oo ooo "
                ],
                "H": [
                    "ooooooo ",
                    "ooooooo ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "I": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o     o "
                ],
                "J": [
                    "    oo  ",
                    "    ooo ",
                    "      o ",
                    "o     o ",
                    "ooooooo ",
                    "oooooo  ",
                    "o       "
                ],
                "K": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "   o    ",
                    "   oo   ",
                    "ooo ooo ",
                    "oo   oo "
                ],
                "L": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "      o ",
                    "     oo ",
                    "    ooo "
                ],
                "M": [
                    "ooooooo ",
                    " oooooo ",
                    "  oo    ",
                    "   oo   ",
                    "  oo    ",
                    " oooooo ",
                    "ooooooo "
                ],
                "N": [
                    "ooooooo ",
                    "ooooooo ",
                    " oo     ",
                    "  oo    ",
                    "   oo   ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "O": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "o     o ",
                    "ooooooo ",
                    " ooooo  "
                ],
                "P": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o    ",
                    "oooo    ",
                    " oo     "
                ],
                "Q": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o   ooo ",
                    "o    oo ",
                    "oooooooo",
                    " ooooo o"
                ],
                "R": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o  o    ",
                    "o  o    ",
                    "ooooooo ",
                    " oo ooo "
                ],
                "S": [
                    " oo  o  ",
                    "oooo oo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "oo oooo ",
                    " o  oo  "
                ],
                "T": [
                    "ooo     ",
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "ooo     "
                ],
                "U": [
                    "oooooo  ",
                    "ooooooo ",
                    "      o ",
                    "      o ",
                    "      o ",
                    "ooooooo ",
                    "oooooo  "
                ],
                "V": [
                    "ooooo   ",
                    "oooooo  ",
                    "     oo ",
                    "      o ",
                    "     oo ",
                    "oooooo  ",
                    "ooooo   "
                ],
                "W": [
                    "ooooooo ",
                    "oooooo  ",
                    "   oo   ",
                    "  oo    ",
                    "   oo   ",
                    "oooooo  ",
                    "ooooooo "
                ],
                "X": [
                    "o     o ",
                    "oo   oo ",
                    " ooooo  ",
                    "  ooo   ",
                    " ooooo  ",
                    "oo   oo ",
                    "o     o "
                ],
                "Y": [
                    "ooo     ",
                    "oooo  o ",
                    "   oooo ",
                    "   oooo ",
                    "oooo  o ",
                    "ooo     "
                ],
                "Z": [
                    "ooo   o ",
                    "oo   oo ",
                    "o   ooo ",
                    "o  oo o ",
                    "o oo  o ",
                    "ooo  oo ",
                    "oo  ooo "
                ],
                "[": [
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "o     o "
                ],
                "\\": [
                    "o       ",
                    "oo      ",
                    " oo     ",
                    "  oo    ",
                    "   oo   ",
                    "    oo  ",
                    "     oo "
                ],
                "]": [
                    "o     o ",
                    "o     o ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "^": [
                    "   o    ",
                    "  oo    ",
                    " oo     ",
                    "oo      ",
                    " oo     ",
                    "  oo    ",
                    "   o    "
                ],
                "_": [
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o"
                ],
                "`": [
                    "oo      ",
                    "o o     "
                ],
                "a": [
                    "     o  ",
                    "  o ooo ",
                    "  o o o ",
                    "  o o o ",
                    "  oooo  ",
                    "   oooo ",
                    "      o "
                ],
                "b": [
                    "o       ",
                    "ooooooo ",
                    "ooooooo ",
                    "   o  o ",
                    "   o  o ",
                    "   oooo ",
                    "    oo  "
                ],
                "c": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o   o ",
                    "  o   o ",
                    "  o   o ",
                    "  oo oo ",
                    "   o o  "
                ],
                "d": [
                    "    oo  ",
                    "   oooo ",
                    "   o  o ",
                    "o  o  o ",
                    "oooooo  ",
                    "ooooooo ",
                    "      o "
                ],
                "e": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o o o ",
                    "  o o o ",
                    "  o o o ",
                    "  ooo o ",
                    "   oo   "
                ],
                "f": [
                    "   o  o ",
                    " oooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "oo      ",
                    " o      "
                ],
                "g": [
                    "   oo   ",
                    "  oooo o",
                    "  o  o o",
                    "  o  o o",
                    "   ooooo",
                    "  ooooo ",
                    "  o     "
                ],
                "h": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "   o    ",
                    "  o     ",
                    "  ooooo ",
                    "   oooo "
                ],
                "i": [
                    "  o   o ",
                    "o ooooo ",
                    "o ooooo ",
                    "      o "
                ],
                "j": [
                    "      o ",
                    "      oo",
                    "       o",
                    "   o   o",
                    " o ooooo",
                    " o oooo "
                ],
                "k": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "    o   ",
                    "   ooo  ",
                    "  oo oo ",
                    "  o   o "
                ],
                "l": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "      o "
                ],
                "m": [
                    "  ooooo ",
                    "  ooooo ",
                    "   o    ",
                    "   oooo ",
                    "  oo    ",
                    "  ooooo ",
                    "   oooo "
                ],
                "n": [
                    "  o     ",
                    "  ooooo ",
                    "   oooo ",
                    "  o     ",
                    "  o     ",
                    "  ooooo ",
                    "   oooo "
                ],
                "o": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o   o ",
                    "  o   o ",
                    "  o   o ",
                    "  ooooo ",
                    "   ooo  "
                ],
                "p": [
                    "  o    o",
                    "  oooooo",
                    "   ooooo",
                    "  o  o o",
                    "  o  o  ",
                    "  oooo  ",
                    "   oo   "
                ],
                "q": [
                    "   oo   ",
                    "  oooo  ",
                    "  o  o  ",
                    "  o  o o",
                    "  oooooo",
                    "  oooooo",
                    "       o"
                ],
                "r": [
                    "  o   o ",
                    "  ooooo ",
                    "   oooo ",
                    "  oo  o ",
                    "  o     ",
                    "  oo    ",
                    "  oo    "
                ],
                "s": [
                    "   o    ",
                    "  ooo o ",
                    "  o o o ",
                    "  o o o ",
                    "  o o o ",
                    "  o ooo ",
                    "     o  "
                ],
                "t": [
                    "  o     ",
                    "  o     ",
                    " ooooo  ",
                    "ooooooo ",
                    "  o   o ",
                    "  o  o  "
                ],
                "u": [
                    "  oooo  ",
                    "  ooooo ",
                    "      o ",
                    "      o ",
                    "  oooo  ",
                    "  ooooo ",
                    "      o "
                ],
                "v": [
                    "  ooo   ",
                    "  oooo  ",
                    "     oo ",
                    "      o ",
                    "     oo ",
                    "  oooo  ",
                    "  ooo   "
                ],
                "w": [
                    "  oooo  ",
                    "  ooooo ",
                    "     oo ",
                    "   ooo  ",
                    "     oo ",
                    "  ooooo ",
                    "  oooo  "
                ],
                "x": [
                    "  o   o ",
                    "  oo oo ",
                    "   ooo  ",
                    "    o   ",
                    "   ooo  ",
                    "  oo oo ",
                    "  o   o "
                ],
                "y": [
                    "  oo    ",
                    "  ooo  o",
                    "    oooo",
                    "     oo ",
                    "    oo  ",
                    "  ooo   ",
                    "  oo    "
                ],
                "z": [
                    "  oo  o ",
                    "  o  oo ",
                    "  o ooo ",
                    "  ooo o ",
                    "  oo  o ",
                    "  o  oo "
                ],
                "{": [
                    "   o    ",
                    " ooooo  ",
                    "ooo ooo ",
                    "o     o ",
                    "o     o "
                ],
                "|": [
                    "ooo ooo ",
                    "ooo ooo "
                ],
                "}": [
                    "o     o ",
                    "o     o ",
                    "ooo ooo ",
                    " ooooo  ",
                    "   o    "
                ],
                "~": [
                    " o      ",
                    "oo      ",
                    "o       ",
                    "oo      ",
                    " o      ",
                    "oo      ",
                    "o       "
                ],
                "\u007f": [
                    "    ooo ",
                    "   oooo ",
                    "  oo  o ",
                    " oo   o ",
                    "  oo  o ",
                    "   oooo ",
                    "    ooo "
                ],
                "\u0080": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0081": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0082": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0083": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0084": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0085": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0086": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0087": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0088": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0089": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008a": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008b": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008c": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008d": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008e": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008f": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0090": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0091": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0092": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0093": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0094": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0095": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0096": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0097": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0098": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0099": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009a": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009b": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009c": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009d": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009e": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009f": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a0": [
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        "
                ],
                "\u00a1": [
                    "o ooooo ",
                    "o ooooo "
                ],
                "\u00a2": [
                    "  ooo   ",
                    " ooooo  ",
                    " o   o  ",
                    "ooooooo ",
                    "oo   oo ",
                    " oo oo  ",
                    "  o o   "
                ],
                "\u00a3": [
                    "   o oo ",
                    " oooooo ",
                    "oooooo  ",
                    "o  o oo ",
                    "oo    o ",
                    " o    o ",
                    "     o  "
                ],
                "\u00a4": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a5": [
                    "o  o o  ",
                    "oo o o  ",
                    " oooooo ",
                    " oooooo ",
                    "oo o o  ",
                    "o  o o  "
                ],
                "\u00a6": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a7": [
                    "      o ",
                    "   oo  o",
                    " oo  o o",
                    "o o  o o",
                    "o o  oo ",
                    "o  oo   ",
                    " o      "
                ],
                "\u00a8": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a9": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00aa": [
                    "     o  ",
                    "o oo o  ",
                    "o oo o  ",
                    "ooo  o  ",
                    " ooo o  ",
                    "     o  "
                ],
                "\u00ab": [
                    "   o    ",
                    "  ooo   ",
                    " oo oo  ",
                    " o o o  ",
                    "  ooo   ",
                    " oo oo  ",
                    " o   o  "
                ],
                "\u00ac": [
                    "  o     ",
                    "  o     ",
                    "  o     ",
                    "  o     ",
                    "  o     ",
                    "  oooo  ",
                    "  oooo  "
                ]
            }
        },
        "Px437 ToshibaSat 8x8": {
            "name": "Px437 ToshibaSat 8x8",
            "height": 8,
            "characters": {
                "!": [
                    " oo     ",
                    "ooooo o ",
                    "ooooo o ",
                    " oo     "
                ],
                "\"": [
                    "ooo     ",
                    "ooo     ",
                    "        ",
                    "ooo     ",
                    "ooo     "
                ],
                "#": [
                    "  o o   ",
                    "ooooooo ",
                    "ooooooo ",
                    "  o o   ",
                    "ooooooo ",
                    "ooooooo ",
                    "  o o   "
                ],
                "$": [
                    "  o     ",
                    " ooo o  ",
                    " o o o  ",
                    "ooooooo ",
                    " o o o  ",
                    " o ooo  ",
                    "    o   "
                ],
                "%": [
                    "oo    o ",
                    "oo   oo ",
                    "    oo  ",
                    "   oo   ",
                    "  oo    ",
                    " oo  oo ",
                    "oo   oo "
                ],
                "&": [
                    "    oo  ",
                    " o oooo ",
                    "oooo  o ",
                    "o ooo o ",
                    "ooo oo  ",
                    " o  ooo ",
                    "   o  o "
                ],
                "'": [
                    "  o     ",
                    "ooo     ",
                    "oo      "
                ],
                "(": [
                    "  ooo   ",
                    " ooooo  ",
                    "oo   oo ",
                    "o     o "
                ],
                ")": [
                    "o     o ",
                    "oo   oo ",
                    " ooooo  ",
                    "  ooo   "
                ],
                "*": [
                    "   o    ",
                    " o o o  ",
                    "  ooo   ",
                    "  ooo   ",
                    " o o o  ",
                    "   o    "
                ],
                "+": [
                    "   o    ",
                    "   o    ",
                    " ooooo  ",
                    " ooooo  ",
                    "   o    ",
                    "   o    "
                ],
                ",": [
                    "       o",
                    "     ooo",
                    "     oo "
                ],
                "-": [
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    "
                ],
                ".": [
                    "     oo ",
                    "     oo "
                ],
                "/": [
                    "      o ",
                    "     oo ",
                    "    oo  ",
                    "   oo   ",
                    "  oo    ",
                    " oo     ",
                    "oo      "
                ],
                "0": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o ooo o ",
                    "o     o ",
                    "ooooooo ",
                    " ooooo  "
                ],
                "1": [
                    "  o   o ",
                    " oo   o ",
                    "ooooooo ",
                    "ooooooo ",
                    "      o ",
                    "      o "
                ],
                "2": [
                    " o    o ",
                    "oo   oo ",
                    "o   ooo ",
                    "o  oo o ",
                    "oooo  o ",
                    " oo   o "
                ],
                "3": [
                    " o   o  ",
                    "oo   oo ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " oo oo  "
                ],
                "4": [
                    "    o   ",
                    "   oo   ",
                    "  ooo   ",
                    " oo o   ",
                    "ooooooo ",
                    "ooooooo ",
                    "    o   "
                ],
                "5": [
                    "ooo  o  ",
                    "ooo  oo ",
                    "o o   o ",
                    "o o   o ",
                    "o o   o ",
                    "o ooooo ",
                    "o  ooo  "
                ],
                "6": [
                    "  oooo  ",
                    " oooooo ",
                    "oo o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  oooo ",
                    "    oo  "
                ],
                "7": [
                    "oo      ",
                    "oo      ",
                    "o   ooo ",
                    "o  oooo ",
                    "o oo    ",
                    "ooo     ",
                    "oo      "
                ],
                "8": [
                    " oo oo  ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " oo oo  "
                ],
                "9": [
                    " oo     ",
                    "oooo  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o oo ",
                    "oooooo  ",
                    " oooo   "
                ],
                ":": [
                    " oo  oo ",
                    " oo  oo "
                ],
                ";": [
                    "       o",
                    " oo  ooo",
                    " oo  oo "
                ],
                "<": [
                    "   o    ",
                    "  ooo   ",
                    " oo oo  ",
                    "oo   oo ",
                    "o     o "
                ],
                "=": [
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  ",
                    "  o  o  "
                ],
                ">": [
                    "o     o ",
                    "oo   oo ",
                    " oo oo  ",
                    "  ooo   ",
                    "   o    "
                ],
                "?": [
                    " o      ",
                    "oo      ",
                    "o  oo o ",
                    "o ooo o ",
                    "ooo     ",
                    " o      "
                ],
                "@": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o ooo o ",
                    "o ooo o ",
                    "ooooo o ",
                    " oooo o "
                ],
                "A": [
                    "  ooooo ",
                    " oooooo ",
                    "oo  o   ",
                    "o   o   ",
                    "oo  o   ",
                    " oooooo ",
                    "  ooooo "
                ],
                "B": [
                    "ooooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "ooooooo ",
                    " oo oo  "
                ],
                "C": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "o     o ",
                    "oo   oo ",
                    " o   o  "
                ],
                "D": [
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "oo   oo ",
                    " ooooo  ",
                    "  ooo   "
                ],
                "E": [
                    "ooooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "o     o "
                ],
                "F": [
                    "ooooooo ",
                    "ooooooo ",
                    "o  o    ",
                    "o  o    ",
                    "o  o    ",
                    "o       "
                ],
                "G": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o  o  o ",
                    "o  o  o ",
                    "oo oooo ",
                    " o oooo "
                ],
                "H": [
                    "ooooooo ",
                    "ooooooo ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "I": [
                    "o     o ",
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "o     o "
                ],
                "J": [
                    "     o  ",
                    "     oo ",
                    "      o ",
                    "o     o ",
                    "ooooooo ",
                    "oooooo  ",
                    "o       "
                ],
                "K": [
                    "ooooooo ",
                    "ooooooo ",
                    "   o    ",
                    "  ooo   ",
                    " oo oo  ",
                    "oo   oo ",
                    "o     o "
                ],
                "L": [
                    "ooooooo ",
                    "ooooooo ",
                    "      o ",
                    "      o ",
                    "      o ",
                    "      o ",
                    "      o "
                ],
                "M": [
                    "ooooooo ",
                    "ooooooo ",
                    " oo     ",
                    "  ooo   ",
                    " oo     ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "N": [
                    "ooooooo ",
                    "ooooooo ",
                    " oo     ",
                    "  oo    ",
                    "   oo   ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "O": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o     o ",
                    "o     o ",
                    "ooooooo ",
                    " ooooo  "
                ],
                "P": [
                    "ooooooo ",
                    "ooooooo ",
                    "o  o    ",
                    "o  o    ",
                    "o  o    ",
                    "oooo    ",
                    " oo     "
                ],
                "Q": [
                    " ooooo  ",
                    "ooooooo ",
                    "o     o ",
                    "o   o o ",
                    "o   oo  ",
                    "oooo oo ",
                    " oooo o "
                ],
                "R": [
                    "ooooooo ",
                    "ooooooo ",
                    "o  o    ",
                    "o  oo   ",
                    "o  ooo  ",
                    "oooo oo ",
                    " oo   o "
                ],
                "S": [
                    " oo  o  ",
                    "oooo oo ",
                    "o  o  o ",
                    "o  o  o ",
                    "o  o  o ",
                    "oo oooo ",
                    " o  oo  "
                ],
                "T": [
                    "o       ",
                    "o       ",
                    "o       ",
                    "ooooooo ",
                    "ooooooo ",
                    "o       ",
                    "o       ",
                    "o       "
                ],
                "U": [
                    "oooooo  ",
                    "ooooooo ",
                    "      o ",
                    "      o ",
                    "      o ",
                    "ooooooo ",
                    "oooooo  "
                ],
                "V": [
                    "ooo     ",
                    "ooooo   ",
                    "   oooo ",
                    "     oo ",
                    "   oooo ",
                    "ooooo   ",
                    "ooo     "
                ],
                "W": [
                    "ooooooo ",
                    "ooooooo ",
                    "    oo  ",
                    "  ooo   ",
                    "    oo  ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "X": [
                    "oo   oo ",
                    "ooo ooo ",
                    "  ooo   ",
                    "   o    ",
                    "  ooo   ",
                    "ooo ooo ",
                    "oo   oo "
                ],
                "Y": [
                    "oo      ",
                    "ooo     ",
                    "  oo    ",
                    "   oooo ",
                    "   oooo ",
                    "  oo    ",
                    "ooo     ",
                    "oo      "
                ],
                "Z": [
                    "o    oo ",
                    "o   ooo ",
                    "o  oo o ",
                    "o  o  o ",
                    "o oo  o ",
                    "ooo   o ",
                    "oo    o "
                ],
                "[": [
                    "ooooooo ",
                    "ooooooo ",
                    "o     o ",
                    "o     o "
                ],
                "\\": [
                    "o       ",
                    "oo      ",
                    " oo     ",
                    "  oo    ",
                    "   oo   ",
                    "    oo  ",
                    "     oo ",
                    "      o "
                ],
                "]": [
                    "o     o ",
                    "o     o ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "^": [
                    "  o     ",
                    " oo     ",
                    "oo      ",
                    "oo      ",
                    " oo     ",
                    "  o     "
                ],
                "_": [
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o",
                    "       o"
                ],
                "`": [
                    "oo      ",
                    "ooo     ",
                    "  o     "
                ],
                "a": [
                    "     o  ",
                    "  o ooo ",
                    "  o o o ",
                    "  o o o ",
                    "  o o o ",
                    "  ooooo ",
                    "   oooo "
                ],
                "b": [
                    "ooooooo ",
                    "ooooooo ",
                    "   o o  ",
                    "  o   o ",
                    "  o   o ",
                    "  ooooo ",
                    "   ooo  "
                ],
                "c": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o   o ",
                    "  o   o ",
                    "  o   o ",
                    "  oo oo ",
                    "   o o  "
                ],
                "d": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o   o ",
                    "  o   o ",
                    "   o o  ",
                    "ooooooo ",
                    "ooooooo "
                ],
                "e": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o o o ",
                    "  o o o ",
                    "  o o o ",
                    "  ooo o ",
                    "   oo o "
                ],
                "f": [
                    "   o    ",
                    " oooooo ",
                    "ooooooo ",
                    "o  o    ",
                    "oo o    ",
                    " o      "
                ],
                "g": [
                    "   oo   ",
                    "  oooo o",
                    "  o  o o",
                    "  o  o o",
                    "   oo  o",
                    "  oooooo",
                    "  ooooo "
                ],
                "h": [
                    "ooooooo ",
                    "ooooooo ",
                    "   o    ",
                    "  o     ",
                    "  o     ",
                    "  ooooo ",
                    "   oooo "
                ],
                "i": [
                    "  o   o ",
                    "o ooooo ",
                    "o ooooo ",
                    "      o "
                ],
                "j": [
                    "      o ",
                    "      oo",
                    "       o",
                    "  o    o",
                    "o oooooo",
                    "o ooooo "
                ],
                "k": [
                    "ooooooo ",
                    "ooooooo ",
                    "    o   ",
                    "   ooo  ",
                    "  oo oo ",
                    "  o   o "
                ],
                "l": [
                    "o     o ",
                    "ooooooo ",
                    "ooooooo ",
                    "      o "
                ],
                "m": [
                    "  ooooo ",
                    "  ooooo ",
                    "  o     ",
                    "   oooo ",
                    "  o     ",
                    "  ooooo ",
                    "   oooo "
                ],
                "n": [
                    "  ooooo ",
                    "  ooooo ",
                    "   o    ",
                    "  o     ",
                    "  o     ",
                    "  ooooo ",
                    "   oooo "
                ],
                "o": [
                    "   ooo  ",
                    "  ooooo ",
                    "  o   o ",
                    "  o   o ",
                    "  o   o ",
                    "  ooooo ",
                    "   ooo  "
                ],
                "p": [
                    "  oooooo",
                    "  oooooo",
                    "   oo   ",
                    "  o  o  ",
                    "  o  o  ",
                    "  oooo  ",
                    "   oo   "
                ],
                "q": [
                    "   oo   ",
                    "  oooo  ",
                    "  o  o  ",
                    "  o  o  ",
                    "   oo   ",
                    "  oooooo",
                    "  oooooo"
                ],
                "r": [
                    "  ooooo ",
                    "  ooooo ",
                    "   o    ",
                    "  o     ",
                    "  o     ",
                    "  o     ",
                    "  o     "
                ],
                "s": [
                    "   o  o ",
                    "  ooo o ",
                    "  o o o ",
                    "  o o o ",
                    "  o o o ",
                    "  o ooo ",
                    "  o  o  "
                ],
                "t": [
                    "  o     ",
                    "oooooo  ",
                    "ooooooo ",
                    "  o   o ",
                    "  o  oo ",
                    "     o  "
                ],
                "u": [
                    "  oooo  ",
                    "  ooooo ",
                    "      o ",
                    "      o ",
                    "     o  ",
                    "  ooooo ",
                    "  ooooo "
                ],
                "v": [
                    "  oo    ",
                    "  oooo  ",
                    "    ooo ",
                    "      o ",
                    "    ooo ",
                    "  oooo  ",
                    "  oo    "
                ],
                "w": [
                    "  oooo  ",
                    "  ooooo ",
                    "     o  ",
                    "   oo   ",
                    "     o  ",
                    "  ooooo ",
                    "  oooo  "
                ],
                "x": [
                    "  o   o ",
                    "  oo oo ",
                    "   ooo  ",
                    "    o   ",
                    "   ooo  ",
                    "  oo oo ",
                    "  o   o "
                ],
                "y": [
                    "  ooo   ",
                    "  oooo o",
                    "     o o",
                    "     o o",
                    "    o  o",
                    "  oooooo",
                    "  ooooo "
                ],
                "z": [
                    "  o   o ",
                    "  o  oo ",
                    "  o ooo ",
                    "  ooo o ",
                    "  oo  o ",
                    "  o   o "
                ],
                "{": [
                    "   o    ",
                    "   o    ",
                    " ooooo  ",
                    "ooo ooo ",
                    "o     o ",
                    "o     o "
                ],
                "|": [
                    "ooo ooo ",
                    "ooo ooo "
                ],
                "}": [
                    "o     o ",
                    "o     o ",
                    "ooo ooo ",
                    " ooooo  ",
                    "   o    ",
                    "   o    "
                ],
                "~": [
                    " o      ",
                    "oo      ",
                    "o       ",
                    "oo      ",
                    " o      ",
                    "oo      ",
                    "o       "
                ],
                "\u007f": [
                    "   ooo  ",
                    "  oooo  ",
                    " oo  o  ",
                    "oo   o  ",
                    " oo  o  ",
                    "  oooo  ",
                    "   ooo  "
                ],
                "\u0080": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0081": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0082": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0083": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0084": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0085": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0086": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0087": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0088": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0089": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008a": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008b": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008c": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008d": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008e": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u008f": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0090": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0091": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0092": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0093": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0094": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0095": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0096": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0097": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0098": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u0099": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009a": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009b": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009c": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009d": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009e": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u009f": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a0": [
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        ",
                    "        "
                ],
                "\u00a1": [
                    "    oo  ",
                    "o ooooo ",
                    "o ooooo ",
                    "    oo  "
                ],
                "\u00a2": [
                    "   oo   ",
                    "  oooo  ",
                    "  o  o  ",
                    "ooo  ooo",
                    "ooo  ooo",
                    "  o  o  ",
                    "  o  o  "
                ],
                "\u00a3": [
                    "   o oo ",
                    " oooooo ",
                    "ooooooo ",
                    "o  o  o ",
                    "oo    o ",
                    " o   oo ",
                    "     o  "
                ],
                "\u00a4": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a5": [
                    "oo  o o ",
                    "ooo o o ",
                    "  oooooo",
                    "  oooooo",
                    "ooo o o ",
                    "oo  o o "
                ],
                "\u00a6": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a7": [
                    " o    o ",
                    "ooooo oo",
                    "o o o  o",
                    "o o  o o",
                    "o  o o o",
                    "oo ooooo",
                    " o    o "
                ],
                "\u00a8": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00a9": [
                    " oooooo ",
                    " oooooo "
                ],
                "\u00aa": [
                    " oo  o  ",
                    "oooo o  ",
                    "o  o o  ",
                    "ooo  o  ",
                    "oooo o  ",
                    "   o o  "
                ],
                "\u00ab": [
                    "   o    ",
                    "  ooo   ",
                    " oo oo  ",
                    " o o o  ",
                    "  ooo   ",
                    " oo oo  ",
                    " o   o  "
                ],
                "\u00ac": [
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   o    ",
                    "   ooo  ",
                    "   ooo  "
                ]
            }
        },
        "Px437_HP_100LX_10x11": {
            "name": "Px437_HP_100LX_10x11",
            "height": 9,
            "characters": {
                "!": [
                    " oo      ",
                    "ooooo oo ",
                    "ooooo oo ",
                    " oo      "
                ],
                "\"": [
                    "oo       ",
                    "ooo      ",
                    "         ",
                    "ooo      ",
                    "oo       "
                ],
                "#": [
                    "  o  o   ",
                    "oooooooo ",
                    "oooooooo ",
                    "  o  o   ",
                    "oooooooo ",
                    "oooooooo ",
                    "  o  o   "
                ],
                "$": [
                    "  o  o   ",
                    " oo  oo  ",
                    " o o  o  ",
                    "oo o  oo ",
                    "oo o  oo ",
                    " oo ooo  ",
                    "  o oo   "
                ],
                "%": [
                    " oo    o ",
                    "ooo   oo ",
                    "o o  oo  ",
                    "ooo oo   ",
                    " oooooooo",
                    "  o  o  o",
                    " oo  oooo",
                    "oo    oo "
                ],
                "&": [
                    "    ooo  ",
                    " ooooooo ",
                    "oooo   o ",
                    "o ooo  o ",
                    "oooooooo ",
                    "   o   o "
                ],
                "'": [
                    "ooo      ",
                    "ooo      "
                ],
                "(": [
                    "  oooo   ",
                    " oooooo  ",
                    "oo    oo "
                ],
                ")": [
                    "o      o ",
                    "oooooooo ",
                    "  oooo   "
                ],
                "*": [
                    "   o     ",
                    "  oo o   ",
                    "  ooo    ",
                    "  oooo   ",
                    "   o     "
                ],
                "+": [
                    "   o     ",
                    "   o     ",
                    "  oooo   ",
                    "  oooo   ",
                    "   o     "
                ],
                ",": [
                    "        o",
                    "      ooo",
                    "      oo "
                ],
                "-": [
                    "   o     ",
                    "   o     ",
                    "   o     ",
                    "   o     ",
                    "   o     "
                ],
                ".": [
                    "      oo ",
                    "      oo "
                ],
                "/": [
                    "      oo ",
                    "     oo  ",
                    "    oo   ",
                    "   oo    ",
                    "  oo     ",
                    " oo      ",
                    " o       "
                ],
                "0": [
                    " oooooo  ",
                    "oooooooo ",
                    "o    o o ",
                    "o  oo  o ",
                    "o oo   o ",
                    "oooooooo ",
                    " oooooo  "
                ],
                "1": [
                    "  o    o ",
                    " oo    o ",
                    "oooooooo ",
                    "oooooooo ",
                    "       o "
                ],
                "2": [
                    " oo   oo ",
                    "oo   ooo ",
                    "o   oo o ",
                    "o   o  o ",
                    "o  oo  o ",
                    "oooo  oo ",
                    " oo   oo "
                ],
                "3": [
                    " o    o  ",
                    "oo    oo ",
                    "o      o ",
                    "o  o   o ",
                    "oo o  oo ",
                    "oooooooo ",
                    " oo ooo  "
                ],
                "4": [
                    "   oo    ",
                    "  ooo    ",
                    "  o o    ",
                    " oo o    ",
                    "oooooooo ",
                    "oooooooo ",
                    "    o  o "
                ],
                "5": [
                    "ooo   o  ",
                    "ooo   oo ",
                    "o o    o ",
                    "o o    o ",
                    "o o    o ",
                    "o oooooo ",
                    "o  oooo  "
                ],
                "6": [
                    " oooooo  ",
                    "oooooooo ",
                    "o  o   o ",
                    "o  o   o ",
                    "o  o   o ",
                    "oo ooooo ",
                    " o  ooo  "
                ],
                "7": [
                    "oo       ",
                    "oo       ",
                    "o        ",
                    "o    ooo ",
                    "o  ooooo ",
                    "oooo     ",
                    "ooo      "
                ],
                "8": [
                    " oo ooo  ",
                    "oooooooo ",
                    "o  o   o ",
                    "o  o   o ",
                    "o  o   o ",
                    "oooooooo ",
                    " oo ooo  "
                ],
                "9": [
                    " oo   o  ",
                    "oooo  oo ",
                    "o  o   o ",
                    "o  o   o ",
                    "o  o   o ",
                    "oooooooo ",
                    " oooooo  "
                ],
                ":": [
                    "  oo  oo ",
                    "  oo  oo "
                ],
                ";": [
                    "        o",
                    "  oo  ooo",
                    "  oo  oo "
                ],
                "<": [
                    "    o    ",
                    "   ooo   ",
                    "  oo oo  ",
                    " oo   ooo",
                    " o      o"
                ],
                "=": [
                    "  o  o   ",
                    "  o  o   ",
                    "  o  o   ",
                    "  o  o   ",
                    "  o  o   "
                ],
                ">": [
                    " o      o",
                    " oo    oo",
                    "  o   oo ",
                    "  ooooo  ",
                    "    o    "
                ],
                "?": [
                    " oo      ",
                    "ooo      ",
                    "oo       ",
                    "o   o oo ",
                    "o ooo oo ",
                    "ooo      ",
                    " oo      "
                ],
                "@": [
                    " oooooo  ",
                    "oooooooo ",
                    "oo    oo ",
                    "o  oo  o ",
                    "oooooo o ",
                    "oooooo o ",
                    " ooooo   "
                ],
                "A": [
                    "  oooooo ",
                    " ooooooo ",
                    "ooo o    ",
                    "o   o    ",
                    "ooo o    ",
                    " ooooooo ",
                    "  oooooo "
                ],
                "B": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o  o   o ",
                    "o  o   o ",
                    "oooooooo ",
                    " oo ooo  "
                ],
                "C": [
                    "  oooo   ",
                    " oooooo  ",
                    "oo    oo ",
                    "o      o ",
                    "o      o ",
                    "oo    oo ",
                    " o    o  "
                ],
                "D": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o      o ",
                    "oo    oo ",
                    " oooooo  ",
                    "  oooo   "
                ],
                "E": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o  o   o ",
                    "o ooo  o ",
                    "o      o ",
                    "oo    oo "
                ],
                "F": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o  o   o ",
                    "o ooo    ",
                    "o        ",
                    "oo       "
                ],
                "G": [
                    "  oooo   ",
                    " oooooo  ",
                    "oo    oo ",
                    "o      o ",
                    "o   o  o ",
                    "oo  oooo ",
                    " o  ooo  "
                ],
                "H": [
                    "oooooooo ",
                    "oooooooo ",
                    "   o     ",
                    "   o     ",
                    "   o     ",
                    "oooooooo ",
                    "oooooooo "
                ],
                "I": [
                    "o      o ",
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o      o "
                ],
                "J": [
                    "    ooo  ",
                    "    oooo ",
                    "      oo ",
                    "       o ",
                    "o     oo ",
                    "oooooooo ",
                    "ooooooo  ",
                    "o        "
                ],
                "K": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o  o   o ",
                    "  ooo    ",
                    " oo oooo ",
                    "ooo  ooo ",
                    "oo     o "
                ],
                "L": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o      o ",
                    "       o ",
                    "       o ",
                    "      oo "
                ],
                "M": [
                    "oooooooo ",
                    "oooooooo ",
                    " oo      ",
                    "  o      ",
                    "  oo     ",
                    " oo      ",
                    "oooooooo ",
                    "oooooooo "
                ],
                "N": [
                    "oooooooo ",
                    "oooooooo ",
                    "ooo      ",
                    "  oo     ",
                    "   ooooo ",
                    "oooooooo ",
                    "oooooooo "
                ],
                "O": [
                    "  oooo   ",
                    " oooooo  ",
                    "oo    oo ",
                    "o      o ",
                    "o      o ",
                    "oo    oo ",
                    " oooooo  ",
                    "  oooo   "
                ],
                "P": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o  o   o ",
                    "o  o     ",
                    "oooo     ",
                    "oooo     ",
                    " oo      "
                ],
                "Q": [
                    "  oooo   ",
                    " oooooo  ",
                    "oo    oo ",
                    "o      o ",
                    "o    ooo ",
                    "oo    oo ",
                    " oooooooo",
                    "  oooo  o"
                ],
                "R": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o  o   o ",
                    "o  oo    ",
                    "oooooo   ",
                    "oooo ooo ",
                    " oo   oo "
                ],
                "S": [
                    " oo   o  ",
                    "oooo  oo ",
                    "oooo   o ",
                    "o  o   o ",
                    "o  oo oo ",
                    "oo ooooo ",
                    " o  ooo  "
                ],
                "T": [
                    "oo       ",
                    "o        ",
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "o        ",
                    "oo       "
                ],
                "U": [
                    "ooooooo  ",
                    "oooooooo ",
                    "      oo ",
                    "       o ",
                    "      oo ",
                    "oooooooo ",
                    "ooooooo  "
                ],
                "V": [
                    "ooo      ",
                    "ooooo    ",
                    "   oooo  ",
                    "     ooo ",
                    "   ooooo ",
                    "ooooo    ",
                    "ooo      "
                ],
                "W": [
                    "ooooo    ",
                    "oooooooo ",
                    "    oooo ",
                    "   ooo   ",
                    "  oooo   ",
                    "    oooo ",
                    "oooooooo ",
                    "ooooo    "
                ],
                "X": [
                    "o      o ",
                    "oo    oo ",
                    "ooo  ooo ",
                    "o oooo o ",
                    "o oooo o ",
                    "ooo  ooo ",
                    "oo    oo ",
                    "o      o "
                ],
                "Y": [
                    "o        ",
                    "ooo      ",
                    "oooo   o ",
                    "  oooooo ",
                    "oooooooo ",
                    "ooo      ",
                    "o        "
                ],
                "Z": [
                    "ooo   oo ",
                    "oo   ooo ",
                    "o   oo o ",
                    "o  oo  o ",
                    "o oo   o ",
                    "ooo   oo ",
                    "oo   ooo "
                ],
                "[": [
                    "oooooooo ",
                    "oooooooo ",
                    "o      o "
                ],
                "\\": [
                    " o       ",
                    " oo      ",
                    "  o      ",
                    "  oo     ",
                    "   ooo   ",
                    "     oo  ",
                    "      oo "
                ],
                "]": [
                    "o      o ",
                    "o      o ",
                    "oooooooo ",
                    "oooooooo "
                ],
                "^": [
                    "  o      ",
                    " oo      ",
                    "oo       ",
                    "ooo      ",
                    "  o      "
                ],
                "_": [
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         "
                ],
                "`": [
                    "o        ",
                    "oo       ",
                    " o       "
                ],
                "a": [
                    "     oo  ",
                    "    oooo ",
                    "  o o  o ",
                    "  o o  o ",
                    "  o oooo ",
                    "  oooooo ",
                    "   ooooo ",
                    "       o "
                ],
                "b": [
                    "o        ",
                    "oooooooo ",
                    "oooooooo ",
                    "   o  o  ",
                    "  o    o ",
                    "  oo  oo ",
                    "  oooooo ",
                    "   oooo  "
                ],
                "c": [
                    "   oooo  ",
                    "  oooooo ",
                    "  oo  oo ",
                    "  o    o ",
                    "  o    o ",
                    "  oo  oo ",
                    "   o  o  "
                ],
                "d": [
                    "   oooo  ",
                    "  oooooo ",
                    "  oo  oo ",
                    "  o    o ",
                    "o oo  oo ",
                    "oooooooo ",
                    "oooooooo ",
                    "       o "
                ],
                "e": [
                    "   oooo  ",
                    "  oooooo ",
                    "  o  o o ",
                    "  o  o o ",
                    "  o  o o ",
                    "  oooo o ",
                    "   ooo   "
                ],
                "f": [
                    "  o    o ",
                    "  o    o ",
                    " ooooooo ",
                    "oooooooo ",
                    "o o    o ",
                    "o        ",
                    "oo       ",
                    " o       "
                ],
                "g": [
                    "   ooo   ",
                    "  ooooo o",
                    "  oo oo o",
                    "  o   o o",
                    "  oo oo o",
                    "   oooooo",
                    "  oooooo ",
                    "  o      "
                ],
                "h": [
                    "o        ",
                    "oooooooo ",
                    "oooooooo ",
                    "   o     ",
                    "  o      ",
                    "  oo     ",
                    "  oooooo ",
                    "   ooooo "
                ],
                "i": [
                    "  o    o ",
                    "  o    o ",
                    "o oooooo ",
                    "o oooooo ",
                    "       o "
                ],
                "j": [
                    "      o  ",
                    "      oo ",
                    "       oo",
                    "        o",
                    "  o    oo",
                    "oooooooo "
                ],
                "k": [
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "    oo o ",
                    "   oo    ",
                    "  ooooo  ",
                    "  o   oo ",
                    "       o "
                ],
                "l": [
                    "o      o ",
                    "o      o ",
                    "oooooooo ",
                    "oooooooo ",
                    "       o "
                ],
                "m": [
                    "  o      ",
                    "  oooooo ",
                    "   ooooo ",
                    "  oo     ",
                    "  oooo   ",
                    "  oooo   ",
                    "  oooooo ",
                    "   ooooo "
                ],
                "n": [
                    "  o      ",
                    "  oooooo ",
                    "  oooooo ",
                    "   o     ",
                    "  o      ",
                    "  oo     ",
                    "  oooooo ",
                    "   ooooo "
                ],
                "o": [
                    "   oooo  ",
                    "  oooooo ",
                    "  oo  oo ",
                    "  o    o ",
                    "  oo  oo ",
                    "  oooooo ",
                    "   oooo  "
                ],
                "p": [
                    "  o     o",
                    "  ooooooo",
                    "   oooooo",
                    "  o   o o",
                    "  o   o  ",
                    "  oo oo  ",
                    "  ooooo  ",
                    "   ooo   "
                ],
                "q": [
                    "   ooo   ",
                    "  ooooo  ",
                    "  oo oo  ",
                    "  o   o  ",
                    "  o   o o",
                    "   oooooo",
                    "  ooooooo",
                    "  o     o"
                ],
                "r": [
                    "  o    o ",
                    "  oooooo ",
                    "   ooooo ",
                    "  oo   o ",
                    "  o      ",
                    "  oo     ",
                    "   o     "
                ],
                "s": [
                    "   o  o  ",
                    "  ooo oo ",
                    "  ooo  o ",
                    "  o o  o ",
                    "  o o  o ",
                    "  o oooo ",
                    "   o oo  "
                ],
                "t": [
                    "  o      ",
                    " oooooo  ",
                    "oooooooo ",
                    "  o   oo ",
                    "  o    o ",
                    "      oo ",
                    "      o  "
                ],
                "u": [
                    "  ooooo  ",
                    "  oooooo ",
                    "      oo ",
                    "       o ",
                    "      oo ",
                    "  oooooo ",
                    "  oooooo ",
                    "       o "
                ],
                "v": [
                    "  ooo    ",
                    "  oooo   ",
                    "     oo  ",
                    "      oo ",
                    "     ooo ",
                    "  oooo   ",
                    "  ooo    "
                ],
                "w": [
                    "  oooo   ",
                    "  oooooo ",
                    "      oo ",
                    "    ooo  ",
                    "    oooo ",
                    "  oooooo ",
                    "  oooo   "
                ],
                "x": [
                    "  o    o ",
                    "  oo  oo ",
                    "   oooo  ",
                    "    oo   ",
                    "   oooo  ",
                    "  oo  oo ",
                    "  o    o "
                ],
                "y": [
                    "  oooo   ",
                    "  ooooo o",
                    "     oo o",
                    "      o o",
                    "     oo o",
                    "  ooooooo",
                    "  oooooo "
                ],
                "z": [
                    "  oo  oo ",
                    "  oo  oo ",
                    "  o  ooo ",
                    "  o  o o ",
                    "  ooo  o ",
                    "  oo  oo ",
                    "  oo  oo "
                ],
                "{": [
                    "   o     ",
                    " oooooo  ",
                    "ooo oooo ",
                    "o      o "
                ],
                "|": [
                    "oooooooo ",
                    "oooooooo "
                ],
                "}": [
                    "o      o ",
                    "o      o ",
                    "ooo oooo ",
                    " oooooo  "
                ],
                "~": [
                    " o       ",
                    "oo       ",
                    "o        ",
                    "oo       ",
                    " oo      ",
                    " oo      ",
                    " o       "
                ],
                "\u007f": [
                    "   ooooo ",
                    "  oooooo ",
                    "  o    o ",
                    " oo    o ",
                    " oo    o ",
                    "  oooooo ",
                    "   ooooo "
                ],
                "\u0080": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0081": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0082": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0083": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0084": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0085": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0086": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0087": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0088": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0089": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u008a": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u008b": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u008c": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u008d": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u008e": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u008f": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0090": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0091": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0092": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0093": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0094": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0095": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0096": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0097": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0098": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u0099": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u009a": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u009b": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u009c": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u009d": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u009e": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u009f": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u00a0": [
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         ",
                    "         "
                ],
                "\u00a1": [
                    "    ooo  ",
                    "oooooooo ",
                    "oooooooo "
                ],
                "\u00a2": [
                    "   oooo  ",
                    "  oooooo ",
                    "  oo  oo ",
                    "  o    oo",
                    "  o    oo",
                    "  oo  oo ",
                    "   o  o  "
                ],
                "\u00a3": [
                    "   o  oo ",
                    "  oooooo ",
                    " ooooooo ",
                    "oo o   o ",
                    "oo o   o ",
                    " o    o  "
                ],
                "\u00a4": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u00a5": [
                    "o  o o   ",
                    "oo o o   ",
                    " ooo o   ",
                    "  oooooo ",
                    " ooooooo ",
                    "oo o o   ",
                    "o  o o   "
                ],
                "\u00a6": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u00a7": [
                    " ooooo  o",
                    "ooooooo  ",
                    "o o   o  ",
                    "o ooooooo",
                    " o ooo oo"
                ],
                "\u00a8": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u00a9": [
                    "oooooooo ",
                    "o      o ",
                    "oooooooo "
                ],
                "\u00aa": [
                    " oo o    ",
                    "ooo o    ",
                    "o o o    ",
                    "ooo o    ",
                    " oo o    "
                ],
                "\u00ab": [
                    "   o     ",
                    "  ooo    ",
                    "  o oo   ",
                    "  o  o   ",
                    "  ooo    ",
                    "  o oo   ",
                    "  o  o   "
                ],
                "\u00ac": [
                    "   oo    ",
                    "   oo    ",
                    "   oo    ",
                    "   oo    ",
                    "   oo    ",
                    "   ooooo ",
                    "   ooooo "
                ]
            }
        },
        "CG Pixel 4x5": {
            "name": "CG Pixel 4x5",
            "height": 5,
            "characters": {
                "!": [
                    "ooo o"
                ],
                "\"": [
                    "oo   ",
                    "     ",
                    "oo   "
                ],
                "#": [
                    "ooooo",
                    " o o ",
                    "ooooo",
                    " o o "
                ],
                "$": [
                    " o  o",
                    "o ooo",
                    "ooo o",
                    "o  o "
                ],
                "%": [
                    "o  o ",
                    "o o  ",
                    "  o o",
                    " o  o"
                ],
                "&": [
                    " o o ",
                    "o o o",
                    " o o ",
                    "    o"
                ],
                "'": [
                    "oo   "
                ],
                "(": [
                    " ooo ",
                    "o   o"
                ],
                ")": [
                    "o   o",
                    " ooo "
                ],
                "*": [
                    "o o o",
                    " ooo ",
                    " ooo ",
                    "o o o"
                ],
                "+": [
                    "  o  ",
                    " ooo ",
                    "  o  "
                ],
                ",": [
                    "    o",
                    "   o "
                ],
                "-": [
                    "  o  ",
                    "  o  ",
                    "  o  "
                ],
                ".": [
                    "    o"
                ],
                "/": [
                    "   oo",
                    "  o  ",
                    "oo   "
                ],
                "0": [
                    " ooo ",
                    "o o o",
                    "oo  o",
                    " ooo "
                ],
                "1": [
                    " o   ",
                    "ooooo"
                ],
                "2": [
                    " o  o",
                    "o  oo",
                    "o o o",
                    " o  o"
                ],
                "3": [
                    "o   o",
                    "o o o",
                    "o o o",
                    " o o "
                ],
                "4": [
                    "ooo  ",
                    "  o  ",
                    "  o  ",
                    "ooooo"
                ],
                "5": [
                    "ooo o",
                    "o o o",
                    "o o o",
                    "o  o "
                ],
                "6": [
                    " ooo ",
                    "o o o",
                    "o o o",
                    "   o "
                ],
                "7": [
                    "o    ",
                    "o    ",
                    "o ooo",
                    "oo   "
                ],
                "8": [
                    " o o ",
                    "o o o",
                    "o o o",
                    " o o "
                ],
                "9": [
                    " o   ",
                    "o o o",
                    "o o o",
                    " ooo "
                ],
                ":": [
                    " o o "
                ],
                ";": [
                    " o oo"
                ],
                "<": [
                    "  o  ",
                    " o o ",
                    "o   o"
                ],
                "=": [
                    " o o ",
                    " o o ",
                    " o o "
                ],
                ">": [
                    "o   o",
                    " o o ",
                    "  o  "
                ],
                "?": [
                    "o    ",
                    "o o o",
                    " o   "
                ],
                "@": [
                    " ooo ",
                    "o   o",
                    "o o o",
                    " oo o"
                ],
                "A": [
                    " oooo",
                    "o o  ",
                    "o o  ",
                    " oooo"
                ],
                "B": [
                    "ooooo",
                    "o o o",
                    "o o o",
                    " o o "
                ],
                "C": [
                    " ooo ",
                    "o   o",
                    "o   o",
                    " o o "
                ],
                "D": [
                    "ooooo",
                    "o   o",
                    "o   o",
                    " ooo "
                ],
                "E": [
                    "ooooo",
                    "o o o",
                    "o o o",
                    "o   o"
                ],
                "F": [
                    "ooooo",
                    "o o  ",
                    "o o  ",
                    "o    "
                ],
                "G": [
                    " ooo ",
                    "o   o",
                    "o o o",
                    "  oo "
                ],
                "H": [
                    "ooooo",
                    "  o  ",
                    "  o  ",
                    "ooooo"
                ],
                "I": [
                    "ooooo"
                ],
                "J": [
                    "   o ",
                    "    o",
                    "    o",
                    "oooo "
                ],
                "K": [
                    "ooooo",
                    "  o  ",
                    " o o ",
                    "o   o"
                ],
                "L": [
                    "ooooo",
                    "    o",
                    "    o",
                    "    o"
                ],
                "M": [
                    "ooooo",
                    " o   ",
                    " o   ",
                    "ooooo"
                ],
                "N": [
                    "ooooo",
                    " o   ",
                    "  o  ",
                    "ooooo"
                ],
                "O": [
                    " ooo ",
                    "o   o",
                    "o   o",
                    " ooo "
                ],
                "P": [
                    "ooooo",
                    "o o  ",
                    "o o  ",
                    " o   "
                ],
                "Q": [
                    " ooo ",
                    "o   o",
                    "o  oo",
                    " oooo"
                ],
                "R": [
                    "ooooo",
                    "o o  ",
                    "o oo ",
                    " o  o"
                ],
                "S": [
                    " o  o",
                    "o o o",
                    "o o o",
                    "o  o "
                ],
                "T": [
                    "o    ",
                    "ooooo",
                    "o    "
                ],
                "U": [
                    "oooo ",
                    "    o",
                    "    o",
                    "oooo "
                ],
                "V": [
                    "oooo ",
                    "    o",
                    "oooo "
                ],
                "W": [
                    "ooooo",
                    "   o ",
                    "   o ",
                    "ooooo"
                ],
                "X": [
                    "oo oo",
                    "  o  ",
                    "  o  ",
                    "oo oo"
                ],
                "Y": [
                    "oo   ",
                    "  ooo",
                    "oo   "
                ],
                "Z": [
                    "o  oo",
                    "o o o",
                    "o o o",
                    "oo  o"
                ],
                "[": [
                    "ooooo",
                    "o   o"
                ],
                "\\": [
                    "oo   ",
                    "  o  ",
                    "   oo"
                ],
                "]": [
                    "o   o",
                    "ooooo"
                ],
                "^": [
                    " o   ",
                    "o    ",
                    " o   "
                ],
                "_": [
                    "    o",
                    "    o",
                    "    o",
                    "    o"
                ],
                "`": [
                    "o    ",
                    " o   "
                ],
                "a": [
                    " oooo",
                    "o o  ",
                    "o o  ",
                    " oooo"
                ],
                "b": [
                    "ooooo",
                    "o o o",
                    "o o o",
                    " o o "
                ],
                "c": [
                    " ooo ",
                    "o   o",
                    "o   o",
                    " o o "
                ],
                "d": [
                    "ooooo",
                    "o   o",
                    "o   o",
                    " ooo "
                ],
                "e": [
                    "ooooo",
                    "o o o",
                    "o o o",
                    "o   o"
                ],
                "f": [
                    "ooooo",
                    "o o  ",
                    "o o  ",
                    "o    "
                ],
                "g": [
                    " ooo ",
                    "o   o",
                    "o o o",
                    "  oo "
                ],
                "h": [
                    "ooooo",
                    "  o  ",
                    "  o  ",
                    "ooooo"
                ],
                "i": [
                    "ooooo"
                ],
                "j": [
                    "   o ",
                    "    o",
                    "    o",
                    "oooo "
                ],
                "k": [
                    "ooooo",
                    "  o  ",
                    " o o ",
                    "o   o"
                ],
                "l": [
                    "ooooo",
                    "    o",
                    "    o",
                    "    o"
                ],
                "m": [
                    "ooooo",
                    " o   ",
                    " o   ",
                    "ooooo"
                ],
                "n": [
                    "ooooo",
                    " o   ",
                    "  o  ",
                    "ooooo"
                ],
                "o": [
                    " ooo ",
                    "o   o",
                    "o   o",
                    " ooo "
                ],
                "p": [
                    "ooooo",
                    "o o  ",
                    "o o  ",
                    " o   "
                ],
                "q": [
                    " ooo ",
                    "o   o",
                    "o  oo",
                    " oooo"
                ],
                "r": [
                    "ooooo",
                    "o o  ",
                    "o oo ",
                    " o  o"
                ],
                "s": [
                    " o  o",
                    "o o o",
                    "o o o",
                    "o  o "
                ],
                "t": [
                    "o    ",
                    "ooooo",
                    "o    "
                ],
                "u": [
                    "oooo ",
                    "    o",
                    "    o",
                    "oooo "
                ],
                "v": [
                    "oooo ",
                    "    o",
                    "oooo "
                ],
                "w": [
                    "ooooo",
                    "   o ",
                    "   o ",
                    "ooooo"
                ],
                "x": [
                    "oo oo",
                    "  o  ",
                    "  o  ",
                    "oo oo"
                ],
                "y": [
                    "oo   ",
                    "  ooo",
                    "oo   "
                ],
                "z": [
                    "o  oo",
                    "o o o",
                    "o o o",
                    "oo  o"
                ],
                "{": [
                    "  o  ",
                    "ooooo",
                    "o   o"
                ],
                "|": [
                    "oo oo"
                ],
                "}": [
                    "o   o",
                    "ooooo",
                    "  o  "
                ],
                "~": [
                    "  o  ",
                    " o   ",
                    "  o  ",
                    " o   "
                ],
                "\u007f": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0080": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0081": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0082": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0083": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0084": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0085": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0086": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0087": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0088": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0089": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u008a": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u008b": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u008c": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u008d": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u008e": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u008f": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0090": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0091": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0092": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0093": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0094": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0095": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0096": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0097": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0098": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u0099": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u009a": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u009b": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u009c": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u009d": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u009e": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u009f": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a0": [
                    "     ",
                    "     ",
                    "     "
                ],
                "\u00a1": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a2": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a3": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a4": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a5": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a6": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a7": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a8": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00a9": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00aa": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00ab": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ],
                "\u00ac": [
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo",
                    "ooooo"
                ]
            }
        }
    }


class DefaultConfig(Config):
    a = []
    for x in range(224, 32, -32):
        a.append([x]*11)
        a.insert(0, [x]*11)
    MODES = {
        'fixed': [  # {'type': 'fixed',
            # 'repeat': a},
            #   {'type': 'weather'},
            #   {'type': 'greeting'},
            {'type': 'fixed',
             'repeat': [[1] * 11, [2] * 11, [3] * 11, [3] * 11, [3] * 11]},
            #   {'type': 'text', 'message': ' Happy Birthday ', 'font': 'simple_6', 'foreground': [
            #   colours.red, colours.orange, colours.yellow, colours.green, colours.indigo, colours.violet], 'background': colours.black},
            {'type': 'text', 'message': ' Happy Birthday Katie! ', 'font': 'simple_8', 'foreground': [
                colours.red, colours.orange, colours.yellow, colours.green, colours.indigo, colours.violet], 'background': colours.black},
            {'type': 'fixed',
             'repeat': [[3] * 11, [2] * 11, [1] * 11, [1] * 11, [1] * 11]},
            #   {'type': 'news'}
        ],
        'meh': [{'type': 'text', 'message': '!',
                 'font': '1x11', 'background': colours.black}], }
