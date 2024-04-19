import pyautogui
import pydirectinput
import time

def map2keyboard(x):
    assert(x==0 or x==1 or x==2)
    if x==0:
        pydirectinput.moveRel(-100, 0, duration=0.5)
    elif x==1:
        pydirectinput.moveRel(100, 0, duration=0.5)
    elif x==2:
        for _ in range(3):
            print(2)
            pydirectinput.press('w')
        # pyautogui.keyDown('W')
        # time.sleep(1)
        # pyautogui.keyUp('W')

def map2keyboard(x):
    assert(x==0 or x==1 or x==2)
    l = ['a', 'd', 'w']
    for _ in range(3):
        pydirectinput.press(l[x])

def main():
    i = 0
    while(1):
        map2keyboard(i)
        i += 1
        i %= 3
        time.sleep(1)


if __name__ == '__main__':
    main()