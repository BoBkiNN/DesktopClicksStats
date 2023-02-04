import pygame
import os
import json
import time
import threading


dbfile = os.getcwd()+os.sep+"db.json"


pygame.init()
scrn = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
LEFT = (66, 245, 66)
RIGHT = (245, 87, 66)
MIDDLE = (218, 66, 245)

imp = pygame.image.load("desktop.png").convert()

scrn.blit(imp, (0, 0))


def loadCl() -> list:
    with open(dbfile) as f:
        j: dict = json.loads(f.read())
    return j["clicks"]

clicks = loadCl()

loop_w = True
def loadloop():
    while loop_w:
        global clicks
        clicks = loadCl()
        time.sleep(1)

loop_th = threading.Thread(target=loadloop)
loop_th.start()

def drawCl(x, y, btn):
    r = 4
    l1s = [x+r, y]
    l1e = [x-r, y]
    if btn == "left":
        color = LEFT
    elif btn == "right":
        color = RIGHT
    else:
        color = MIDDLE
    pygame.draw.line(scrn, color, l1s, l1e)
    l2s = [x, y+r]
    l2e = [x, y-r]
    pygame.draw.line(scrn, color, l2s, l2e)

pygame.display.flip()
running = True
while running:
    for c in clicks:
        c: dict
        drawCl(c["x"], c["y"], c["btn"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_w = False
            running = False

    pygame.display.flip()
    clock.tick(60)
