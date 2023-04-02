#!/usr/bin/env python3
# Horrible code, please ignore or refactor :)
import pygame
from pygame.locals import *
import json
import time

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

pygame.font.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fonts = {"Px437 Sigma RM 8x8": {'height': 8, 'start': 8, 'end': 0},
             "Px437 ToshibaSat 8x8": {'height': 8, 'start': 8, 'end': 0}, "Px437_HP_100LX_10x11": {'height': 11, 'start': 10, 'end': 1}, "CG Pixel 4x5": {'height':5, 'start': 5, 'end': 0}}
    all_fonts = {}
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    for font in fonts:
        height = fonts[font]['height']
        start = fonts[font]['start']
        end= fonts[font]['end']
        myfont = pygame.font.SysFont(font, height)
        fontdef = {"name": font, "height": height}
        fontchars = {}
        for character in range(33,173):
        # for character in range(102, 104):
            displaysurface.fill(BLACK)
            label = myfont.render(chr(character), 0, WHITE)
            displaysurface.blit(label, (1, 1))
            pygame.display.update()
            thisChar = []
            for x in range(1, label.get_width() + 1):
                line = []
                for y in range(start, end, -1):
                    pixel = displaysurface.get_at((x, y))
                    line.insert(0, "o" if pixel[0] == 255 else " ")
                thisChar.append(''.join(line))
            # Trim down the font
            non_blank_indexes=[index for index in range(0,len(thisChar)) if any(x.isalnum() for x in thisChar[index])]
            fontchars[chr(character)] = thisChar[min(non_blank_indexes):max(non_blank_indexes)+1] if len(non_blank_indexes) > 0 else thisChar
        fontdef['characters'] = fontchars
        all_fonts[font] = fontdef
    print(json.dumps(all_fonts, indent=4))
    running = False
