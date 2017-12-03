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
from Tool import *
import random
path = "GoBang.png"
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1500x1100")
        # self.alertButton = tk.Button(self, text='PRESS', command=self.paint_chess)
        # self.alertButton.pack()
        # im.show()
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        Glo.imm=Image.open(path)
        I=array(Glo.imm)
        # for i in range(I.shape()[0]):
        #     for j in range(I.shape()[1]):
        #         for k in range(15):
        #             if()
        for i in range(15):
            # print(I.shape)
            for j in range(1234):
                I[200+i*30][j]=[255,0,0]
        for i in range(15):
            # print(I.shape)
            for j in range(783):
                I[j][200+i*30]=[255,0,0]
        Glo.imm = Image.fromarray(uint8(I))
        self.img = ImageTk.PhotoImage(Glo.imm)
        # print(img.width())
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(image=self.img)
        # self.panel.pack(side = "left", fill = "both", expand = "yes")
        self.panel.pack(side = "left")
        self.update_clock()
        # add title and show the plot
        # self.paint_chess(1,1)

        self.root.mainloop()
    def paint_chess(self,x,y,p):
        Glo.Now[x][y]=p
        I=array(Glo.imm)
        for i in range(200+x*30-5,200+x*30+5):
            for j in range(200+y*30-5,200+y*30+5):
                if(p==1):
                    I[i][j]=[0,255,255]
                else:
                    I[i][j]=[0,0,0]
        Glo.imm = Image.fromarray(uint8(I))
        self.img = ImageTk.PhotoImage(Glo.imm)
        self.panel['image'] = self.img
        # pass
    def update_clock(self):

        # self.label.configure(text=now)
        # print("before grab")
        # print("grab")
        # print("mouse",a,b)
        # print("before write")
        # print(type(self.I))
        # self.img = ImageTk.PhotoImage(self.im)
        # self.panel['image'] = self.img
        a,b=Think(Glo.P)
        self.paint_chess(a,b,Glo.P)
        if WinOrNot(a,b,Glo.Now):
            print(a,b,Glo.P)
            print(Glo.Now)
            return
        if Glo.P==1:
            Glo.P=2
        else:
            Glo.P=1
        self.root.after(10, self.update_clock)

app=App()
