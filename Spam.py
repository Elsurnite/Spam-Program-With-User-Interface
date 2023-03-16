import time
import pyautogui

import tkinter
from tkinter import *
#--------------------------Window Codes-----------------------------#
master = Tk()

master.title('Elsurnite')

canvas = Canvas(master, height=200, width=420)
canvas.pack()

Metin= Label(master, text="Spam Text:", font="Verdana 9 bold")
Metin.place(x=10,y=20)
Metin1= tkinter.Entry(master)
Metin1.place(x=200,y=20)

Sayac= Label(master, text="Countdown:", font="Verdana 9 bold")
Sayac.place(x=10,y=50)


var=IntVar()

buton1 = Radiobutton(master, variable = var, value=2)
buton1.place(x=200,y=50)
Metin= Label(master, text="2", font="Verdana 9 bold")
Metin.place(x=203,y=70)


buton2 = Radiobutton(master, variable = var, value=3)
buton2.place(x=250,y=50)
Metin= Label(master, text="3", font="Verdana 9 bold")
Metin.place(x=253,y=70)

buton3 = Radiobutton(master, variable = var, value=4)
buton3.place(x=300,y=50)
Metin= Label(master, text="4", font="Verdana 9 bold")
Metin.place(x=303,y=70)


Sayac= Label(master, text="Spam Count:", font="Verdana 9 bold")
Sayac.place(x=10,y=85)

var2=IntVar()

buton4 = Radiobutton(master, variable = var2, value=10)
buton4.place(x=200,y=85)
Metin= Label(master, text="10", font="Verdana 9 bold")
Metin.place(x=198,y=105)


buton5 = Radiobutton(master, variable = var2, value=20)
buton5.place(x=250,y=85)
Metin= Label(master, text="20", font="Verdana 9 bold")
Metin.place(x=248,y=105)

buton6 = Radiobutton(master, variable = var2, value=40)
buton6.place(x=300,y=85)
Metin= Label(master, text="40", font="Verdana 9 bold")
Metin.place(x=298,y=105)
#-----------------------------Spam----------------------------------#
def spamyazı():
  a=(Metin1.get())
  b=(var.get())
  c=(var2.get())
  d = 0

  time.sleep(b)
  f = (a) 
  while d < c:
   for line in f:
    pyautogui.typewrite(line)
   if f==a:
     d += 1
     pyautogui.press('enter')
#-------------------------------------------------------------------#
tus = tkinter.Button(master, text="Start Spam",font="Verdana 12 bold", width=25,command=spamyazı)
tus.place(x=70,y=135)
#-------------------------------------------------------------------#
master.mainloop()   