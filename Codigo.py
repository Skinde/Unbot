import pynput, random, time, math, sys
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()




#to confuse the bot detection algorithm
def trickmove(x0, x1, y0, y1):
    moves = random.randint(15, 16)
    while (mouse.position[0] > x1 or mouse.position[0] < x0) or (mouse.position[1] > y1 or mouse.position[1] < y0):
            r = random.randint(-1, 1)
            mouse.move(round((x1-(x1-x0)/2-mouse.position[0])/moves),round((y1-(y1-y0)/2-mouse.position[1])/moves))
            time.sleep(random.randrange(1, 2)/100)
def tricktype(word):
    for n in word:
        keyboard.type(n)
        time.sleep(random.randrange(10, 20)/100)


def buscar(canal):
    trickmove(306, 858, 88, 110)
    r = random.randint(1,2)/10
    time.sleep(0.5+r)
    mouse.press(Button.left)
    time.sleep(0.1+r)
    mouse.release(Button.left)
    time.sleep(0.5+r)
    for i in range(16):
        keyboard.press(Key.backspace)
        time.sleep(random.randrange(10, 20)/100)
    keyboard.release(Key.backspace)
    time.sleep(0.5+r)
    tricktype(canal)
    time.sleep(0.3+r)
    keyboard.press(Key.enter)

print("Para abortar cierra esta ventana")
keyboard.press(Key.alt)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(0.1)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)
while True:
    r = random.randint(1,2)/10
    buscar("Big M's")
    time.sleep(3+r)
    trickmove(135, 797, 300, 350)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3+r)
    trickmove(141, 319, 390, 442)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(180+r)
    buscar("Dani bzrp vol 24")
    time.sleep(3+r)
    trickmove(135, 797, 300, 350)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(176+r)


        

        

