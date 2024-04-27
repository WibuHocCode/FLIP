import pygame as pg, sys
from pygame.locals import *

class Score:
    pg.font.init()
    color = 0
    colorScore = (236, 240, 241)
    level = 0
    score = 0
    timeClick = 0
    noti = ""
    notiRec = ""
    rect = 0
    rectScore = 0
    font = pg.font.Font("C:\Windows\Fonts\8514oem.fon", 80)
    def __init__(self, color, level, score, timeClick, x, y, noti):
        self.color = color
        self.level = level
        self.score = score
        self.noti = noti
        self.timeClick = timeClick
        self.rect = pg.Rect(0, 0, x, y)
        self.rectScore = pg.Rect(0, x, x, y - x)
        self.noti = self.font.render(self.noti, True, (52, 152, 219))
        self.notiRec = self.noti.get_rect()
        self.notiRec.center = (x, y)
