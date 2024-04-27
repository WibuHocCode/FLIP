import pygame as pg, sys
from pygame.locals import *
import icon
import Score
import random

# Variable
running = True
wigWin = 500
heiWin = wigWin + 100
colorBg = (52, 73, 94)
arrayIcon = []
arrayIconChoosed = []
level = 1
score = 0
borderSpace = int(wigWin * 0.1)
iconSpace = 12
fps = 60
image = ["D:\\TT\\Flip\\1.png", "D:\\TT\\Flip\\2.png", "D:\\TT\\Flip\\3.png", "D:\\TT\\Flip\\4.png", "D:\\TT\\Flip\\5.png", "D:\\TT\\Flip\\6.png"]
arrNum = []
special = "D:\\TT\\Flip\\spc.png"
spc = False
timeClick = 2
scoreNoti = Score.Score(colorBg, level, score, 10, wigWin, heiWin, "Level: " + str(level) + "  " + "Score: " + str(score) + "  " + "Click: " + str(timeClick))
font = pg.font.Font("C:\Windows\Fonts\8514oem.fon", 20)

# pygame
pg.init()
win = pg.display.set_mode((wigWin, heiWin))
pg.display.set_caption("PIKACHU")
win.fill(colorBg)
clock = pg.time.Clock()

# Function
def makePos(level):
    pos = []
    for i in range(level + 1):
        for j in range(level + 1):
            pos.append([i, j])
    return pos

def heiIcon(level):
    return int((wigWin - (2 * (borderSpace) + (level * iconSpace))) / (level + 1))

def colli(x, y, hei):
    color = (96, 163, 188)
    colorBd = (229, 80, 57)
    rec = pg.Rect(x, y, hei, hei)
    recBd = pg.Rect(x - 2, y - 2, hei + 4, hei + 4)
    pg.draw.rect(win, colorBd, recBd, border_radius=5)
    pg.draw.rect(win, color, rec, border_radius=5)
    
def makeArrNum(num):
    global arrNum
    for i in range(int(num / 2)):
        n = random.randint(0, len(image)-1)
        arrNum.append(n)
        arrNum.append(n)
    if len(arrNum) < num:
        arrNum.append(-1)

def makeArrayIcon():
    global arrayIcon
    for i in range(len(makePos(level))):
        num = random.randint(0, len(arrNum) - 1)
        if arrNum[num] != -1:
            arrayIcon.append(icon.icon(borderSpace + makePos(level)[i][0] * (heiIcon(level) + iconSpace), borderSpace + makePos(level)[i][1] * (heiIcon(level) + iconSpace), heiIcon(level), image[arrNum[num]]))
        else:
            arrayIcon.append(icon.icon(borderSpace + makePos(level)[i][0] * (heiIcon(level) + iconSpace), borderSpace + makePos(level)[i][1] * (heiIcon(level) + iconSpace), heiIcon(level), special))
        arrNum.pop(num)
        
def choosed(image, x, y, hei):
    img = pg.image.load(image)
    img = pg.transform.scale(img, (hei, hei))
    win.blit(img, (x, y))

def makeScore(level):
    global scoreNoti
    scoreNoti = Score.Score(colorBg, level, score, 10, wigWin, heiWin, "Level: " + str(level) + "  " + "Score: " + str(score) + "  " + "Click: " + str(timeClick))

        
makeArrNum((level + 1) ** 2)
makeArrayIcon()
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for i in arrayIcon:
                if i.getRec().collidepoint(pg.mouse.get_pos()) and i.getImage() == "D:\\TT\\Flip\\spc.png":
                    arrayIcon.remove(i)
                    spc = True
                if i.getRec().collidepoint(pg.mouse.get_pos()) and i not in arrayIconChoosed and i.getImage() != "D:\\TT\\Flip\\spc.png":
                    arrayIconChoosed.append(i)
                    if len(arrayIconChoosed) == 2:
                        timeClick -= 1
                        choosed(i.getImage(), i.getPos()[0], i.getPos()[1], i.getHei())
                        pg.display.update()
                        pg.time.delay(200)        
                        if arrayIconChoosed[0].getImage() == arrayIconChoosed[1].getImage():
                            arrayIcon.remove(arrayIconChoosed[0])
                            arrayIcon.remove(arrayIconChoosed[1])
                            arrayIconChoosed = []
                            score += 5
                            timeClick += 1
                        else:
                            arrayIconChoosed = []
            if len(arrayIcon) == 0:
                level += 1
                if level > 5:
                    level = 5
                arrNum = []
                arrayIconChoosed = []
                arrayIcon = []
                makeArrNum((level + 1) ** 2)
                makeArrayIcon()
                timeClick = int((level + 1) ** 2 * (2 / 3))
    
    
                
    makeScore(level)
    pg.draw.rect(win, scoreNoti.color, scoreNoti.rect)   
    pg.draw.rect(win, scoreNoti.colorScore, scoreNoti.rectScore, border_radius=5)
    win.blit(scoreNoti.noti, (0, wigWin))         
    # Draw icon
    for i in arrayIcon:
        pg.draw.rect(win, i.getColorBd(), i.getRecBd(), border_radius=5)
        pg.draw.rect(win, i.getColor(), i.getRec(), border_radius=5)
        
    # Chọn
    for i in arrayIcon:
        if (i.getRec().collidepoint(pg.mouse.get_pos())):
            colli(i.getPos()[0], i.getPos()[1], i.getHei())
        if i in arrayIconChoosed:
            colli(i.getPos()[0], i.getPos()[1], i.getHei())
            choosed(i.getImage(), i.getPos()[0], i.getPos()[1], i.getHei())
        if i.getImage() == "D:\\TT\\Flip\\spc.png":
            colli(i.getPos()[0], i.getPos()[1], i.getHei())
            choosed(i.getImage(), i.getPos()[0], i.getPos()[1], i.getHei())
            
    if timeClick <= 0:
        Con = True
        while Con:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        # print(timeClick)
                        arrayIcon = []
                        arrayIconChoosed = []
                        timeClick = 2
                        level = 1
                        score = 0
                        scoreNoti = Score.Score(colorBg, level, score, 10, wigWin, heiWin, "Level: " + str(level) + "  " + "Score: " + str(score) + "  " + "Click: " + str(timeClick))
                        makeArrNum((level + 1) ** 2)
                        makeArrayIcon()
                        Con = False
            notiLose = font.render("YOU LOSE PRESS --SPACE-- TO TRY AGAIN", True, (52, 152, 219))
            notiLoseRec = notiLose.get_rect()
            notiLoseRec.center = (wigWin // 2, heiWin // 2)
            win.blit(notiLose, notiLoseRec)
            pg.display.update()
            
    clock.tick(fps)
    pg.display.update()
