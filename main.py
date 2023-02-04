import json
import os
import threading
import time
from datetime import datetime

from pynput import mouse, keyboard
from win32gui import GetForegroundWindow, GetWindowText

print("starting")

listener = None

desktop_id = 65888
dbfile = os.getcwd()+os.sep+"db.json"
buffer: list = []
loop_w = True

def startup():
    global desktop_id
    kb: keyboard.Listener = None
    print("Press Enter after desktop click")
    def press_cb(key: keyboard.Key):
        global desktop_id
        # print(type(key), key)
        if key == keyboard.Key.enter:
            desktop_id = GetForegroundWindow()
            print(f"Desktop id set: {desktop_id}")
            return False
        print("Press Enter after desktop click")
        
    kb = keyboard.Listener(on_press=press_cb)
    kb.start()
    kb.join()
startup()


def checkDb():
    if not os.path.exists(dbfile):
        with open(dbfile, "w") as f:
            f.write("{}")
            f.close()

def asloop():
    while loop_w:
        checkDb()
        if len(buffer) == 0:
            print("skipping")
            time.sleep(10)
            continue
        print("saving")
        j = json.loads(open(dbfile).read())
        try:
            j["clicks"]
        except:
            print("clicks not exists")
            j["clicks"] = []
        cls: list = j["clicks"]
        for i in buffer.copy():
            # print(buffer)
            cls.append(i)
            buffer.remove(i)
        j["clicks"] = cls
        with open(dbfile,"w") as f:
            f.write(json.dumps(j, indent=4))
        time.sleep(10)

loopth = threading.Thread(target=asloop, name="SaveLoop")
loopth.start()

def getActiveWindow():
    w = GetForegroundWindow()
    print(f"Window {w}:", GetWindowText(w))
    return None if w == desktop_id else w

def stop():
    global loop_w
    loop_w = False
    listener.stop()

def on_move(x, y):
    # print(f'Pointer moved to {(x, y)}')
    pass

def on_click(x: int, y: int, button: mouse.Button, pressed: bool):
    aw = getActiveWindow()
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    clobj = {"x":x, "y": y, "btn": button.name, "time": now}
    if aw is None and pressed:
        print("New click added:", clobj)
        buffer.append(clobj)
    else:
        print(clobj)
        
    

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1} d: {2}'.format(
        'down' if dy < 0 else 'up',
        (x, y), (dx, dy)))
    # if dy < 0:
    #     stop()

listener = mouse.Listener(on_click=on_click)

listener.start()