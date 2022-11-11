from ast import parse
from re import T
import pyautogui as pg
import time
t = input("how much time do you need? :")
text = input("what is your text? :")
repeat = input("how many times? :")

time.sleep(int(t))
for i in range(int(repeat)):
    time.sleep(1)
    print(int(repeat)-(i+1))
    pg.write(text)
    pg.press('Enter')
