import pygame as pg, sys
from pygame.locals import *

class icon:
    x = 0
    y = 0
    hei = 0
    Rec = pg.Rect(x, y, hei, hei)
    recBd = pg.Rect(x, y, hei, hei)
    color = (189, 195, 199)
    colorBd = (229, 80, 57)
    image = ""

    def __init__(self, x, y, hei, image):
        self.x = x
        self.y = y
        self.hei = hei
        self.Rec = pg.Rect(x, y, hei, hei)
        self.recBd = pg.Rect(x - 2, y - 2, hei + 4, hei + 4)
        self.image = image

    def getPos(self):
        return [self.x, self.y]
    
    def getHei(self):
        return self.hei
    
    def getRec(self):
        return self.Rec
    
    def getRecBd(self):
        return self.recBd
      
    def getColor(self):
        return self.color
    
    def getColorBd(self):
        return self.colorBd 
    
    def getImage(self):
        return self.image
