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
def WinOrNot(x, y,C):
    if(spread(x,y,1,0,C)+spread(x,y,-1,0,C)>=4):
        return True
    if(spread(x,y,1,1,C)+spread(x,y,-1,-1,C)>=4):
        return True
    if(spread(x,y,1,-1,C)+spread(x,y,-1,1,C)>=4):
        return True
    if(spread(x,y,0,1,C)+spread(x,y,0,-1,C)>=4):
        return True
    return False


def spread(x, y, dir1, dir2,C):
    pace = 0
    while (True):
        x += dir1;
        y += dir2
        if (outborder(x, y) or C[x][y] != C[x - dir1][y - dir2]):
            return pace
        pace += 1

def outborder(x, y):
    if (x < 0 or x > 14 or y < 0 or y > 14):
        return True

def Search(x, y, player):
    sup=copy(Glo.Now)
    sup[x][y]=player
    random.seed()
    p1=0
    p2=0
    for i in range(1000):
        o=Play(sup,player)
        if o==1:
            p1+=1
        else:
            p2+=1
    # print(Glo.Now)
    if player==1:
        return p1/1000.0
    else:
        return p2/1000.0
    # return random.random()
def Play(sup,player):
    while(True):
        r1 = random.random()
        r2 = random.random()
        x = int(r1 * 15)
        y = int(r2 * 15)
        sup[x][y]=player
        if WinOrNot(x,y,sup):
            return player
        if player==1:
            player=2
        if player==2:
            player=1

def Think(player):
    random.seed()
    rate = []
    xL = []
    yL = []
    for i in range(100):
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
