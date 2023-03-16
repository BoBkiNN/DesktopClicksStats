from PIL import Image, ImageDraw
import os
import json
import time
import threading


dbfile = os.getcwd()+os.sep+"db.json"



LEFT = (66, 245, 66)
RIGHT = (245, 87, 66)
MIDDLE = (218, 66, 245)

try:
    imp = Image.open("desktop.png")
except:
    imp = Image.new(mode="RGBA", size=(1920, 1080), color=(0, 0, 0, 0))
imd = ImageDraw.Draw(imp)


def loadCl() -> list:
    with open(dbfile) as f:
        j: dict = json.loads(f.read())
    return j["clicks"]

clicks = loadCl()

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
    cords1 = [tuple(l1s), tuple(l1e)]
    imd.line(cords1, fill=color, width=1)
    l2s = [x, y+r]
    l2e = [x, y-r]
    cords2 = [tuple(l2s), tuple(l2e)]
    imd.line(cords2, fill=color, width=1)

for c in clicks:
    c: dict
    drawCl(c["x"], c["y"], c["btn"])

imp.save(os.getcwd()+os.sep+"render.png", optimize=False)
