import ch9329Comm
import serial
import time

def sendMsg(x):
    assert(x==0 or x==1 or x==2)
    lst = ["QQ", "RR", "WW"]
    keyboard = ch9329Comm.keyboard.DataComm()
    keyboard.send_data(lst[x])
    keyboard.release()

def sendMouseMsg(dir, dis, x, y):
    '''
    Args:
        dir: direction the mouse to move. Options: 0 -> left, 1 -> right.
        dis: how many pixels the mouse will move.
        (x, y): resolution of your screen.
    '''
    assert(dir==0 or dir==1)
    lst = [-dis, dis]
    mouse = ch9329Comm.mouse.DataComm(x,y)
    mouse.send_data_relatively(lst[dir], 0) # not to change y value by default
    # mouse.click()

if __name__ == '__main__':
    serial.ser = serial.Serial('COM8', 115200)
    x = 0
    cnt = 0
    resolution = {
        "x": 1920,
        "y": 1080
    }
    while cnt<10:
        x += 1
        cnt += 1
        x %= 2
        print(x)
        time.sleep(1)
        # sendMsg(x)
        sendMouseMsg(x, 100, resolution["x"], resolution["y"])

    serial.ser.close()
