from math import fabs
from tkinter import * 
from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=700, height=600, background="white")
tahvel.grid()

#Harjutus. Lipud.
#1-Флаг
#30-отступ от края, 50-отступ сверху, 300-ширина, 100-нижния линия
tahvel.create_rectangle(630,50, 350,100,fill="#1F85DE")
tahvel.create_rectangle(630,100, 350,150,fill="#000000")
tahvel.create_rectangle(630,200, 350,150,fill="#ffffff")
#2-Флаг
tahvel.create_rectangle(30,50, 300,100,fill="#17a2c0")
tahvel.create_rectangle(30,100, 300,150,fill="#e2da27")
tahvel.create_rectangle(30,200, 300,150,fill="#17a2c0")
#треугольник
tahvel.create_polygon(30,50, 100,125, 30,200,fill="black")
#3-Флаг
tahvel.create_rectangle(30,250,  300,300,fill="white")
tahvel.create_rectangle(30,350,  300,300,fill="red")






#from tkinter import *
#from tkinter import font # vajalik teksti fondi muutmiseks

#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="white")
#tahvel.grid()

## üksik kriips (x0, y0, x1, y1)
#tahvel.create_line(30, 40, 300, 40)

# ühendatud kriipsud (suvaline arv koordinaatide paare)
#tahvel.create_line(30,60,  300,60,  300,100,  70,100)

## võimalik on muuta joone paksust (width) ja sisu värvi (fill)
#tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

## teistsugune joone stiil
#tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

## tõmbab kriipsud, ühendab otsapunktid ja värvib sisu
## värve saab määrata ka rgb komponentidena
## vt. http://www.colorpicker.com/
#tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")

## ristkülik
#tahvel.create_rectangle(30,260,  300,450)

## ovaal
#tahvel.create_oval(30,260,  300,450, width=2, outline="blue", fill="wheat")

## proovi liigutada hiirt selle ovaali kohale
#tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

## kui soovid teksti esitamisel ise fonti valida, siis tuleb enne vastav font luua
#suur_font = font.Font(family='Helvetica', size=32, weight='bold')
#tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)

#raam.mainloop()
raam.mainloop()
