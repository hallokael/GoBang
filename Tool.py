# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time
from pyautogui import *
import tkinter.messagebox as messagebox
from time import sleep
from PIL import Image,ImageTk
from PIL import ImageGrab
from numpy import *
from pylab import *
import Glo
import random
def WinOrNot(x, y):
    if(spread(x,y,1,0)+spread(x,y,-1,0)>=4):
        return True
    if(spread(x,y,1,1)+spread(x,y,-1,-1)>=4):
        return True
    if(spread(x,y,1,-1)+spread(x,y,-1,1)>=4):
        return True
    if(spread(x,y,0,1)+spread(x,y,0,-1)>=4):
        return True
    return False


def spread(x, y, dir1, dir2):
    pace = 0
    while (True):
        x += dir1;
        y += dir2
        if (outborder(x, y) or Glo.Now[x][y] != Glo.Now[x - dir1][y - dir2]):
            return pace
        pace += 1

def outborder(x, y):
    if (x < 0 or x > 14 or y < 0 or y > 14):
        return True


def Search(x, y, player):
    return random.random()


def Think(player):
    random.seed()
    rate = []
    xL = []
    yL = []
    for i in range(20):
        r1 = random.random()
        r2 = random.random()
        x = int(r1 * 15)
        y = int(r2 * 15)
        if Glo.Now[x][y] != 0:
            i -= 1
            continue
        xL.append(x)
        yL.append(y)
        rat = Search(x, y, player)
        rate.append(rat)
    maxi = -1
    maxrate = -1
    for i in range(len(rate)):
        if rate[i] > maxrate:
            maxrate = rate[i]
            maxi = i
    return xL[maxi], yL[maxi]
