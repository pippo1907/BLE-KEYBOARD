import time
import keyboard
import pyautogui
import os
from datetime import datetime
from plyer import notification

import serial

ser = serial.Serial("COM6", 115200, timeout=1)


def btn1():
    #Takes screen shot
    print("Button 4 pressed")
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(filename)
    notification.notify(
        title="Screenshot Taken",
        message=f"Saved as {filename}",
        timeout=3
    )
    print(f"Saved: {filename}")


def btn2():
    #split screen
    print("Button 2 pressed")
    keyboard.press_and_release("windows+left")
    time.sleep(1)
    keyboard.press_and_release("tab")
    keyboard.press_and_release("enter")

def btn3():
    #kuch nhi krta upcoming ice cream
    print("button 1 pressed")
    os.system("start https://blinkit.com/checkout")


def btn4():
    print("Buttton 3 pressed")
    # os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    # os.system("rundll32.exe user32.dll,LockWorkStation")
    keyboard.press_and_release("windows+d")

while True:
    cmd = ser.readline().decode().strip()
    # print(cmd)
    # if(cmd.lower()=="snip"):
    #     os.startfile(r"C:\Users\omish\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe")

    if cmd == "1":
        btn1()

    elif cmd == "2":
        btn2()

    elif cmd == "3":
        btn3()

    elif cmd == "4":
        btn4()
    else:
        print("Unknown command:", cmd)