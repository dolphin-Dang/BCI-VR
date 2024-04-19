Trying to map signals from DL models to auto-keyboard press-down signals. 
+ Software way is simple but can be blocked by some full-screen games.
+ Hardware way can do all things w/o being blocked.

`map2keyboard.py`: This is a software map, using `PyAutoGui` package.

`hardwareMap.py`: This is a hardware map from software control signal to keyboard signal, using `ch9329Comm` device. To better use this .py file, U need to change the serial due to your own computer. You may look up details from your `Device Manager` -> `COM`.

Useful link: https://github.com/beijixiaohu/CH9329_COMM.
