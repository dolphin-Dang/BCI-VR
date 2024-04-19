import ch9329Comm
import serial
import time

def sendMsg(x):
    assert(x==0 or x==1 or x==2)
    lst = ["QQ", "RR", "WW"]
    keyboard = ch9329Comm.keyboard.DataComm()
    keyboard.send_data(lst[x])
    keyboard.release()


if __name__ == '__main__':
    serial.ser = serial.Serial('COM8', 115200)
    x = 0
    cnt = 0
    while cnt<10:
        x += 1
        cnt += 1
        x %= 3
        print(x)
        time.sleep(1)
        sendMsg(x)

    serial.ser.close()