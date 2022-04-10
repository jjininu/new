from __future__ import annotations
import tkinter
import numpy as np
from  rozy import *


def click_1():

    if lbl['text'] != '':
        global f
        entry1.insert("end", str(1))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(1))
        g = entry1.get()

def click_2():

    if lbl['text'] != '':
        global f
        entry1.insert("end", str(2))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(2))
        g = entry1.get()


def click_3():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(3))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(3))
        g = entry1.get()


def click_4():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(4))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(4))
        g = entry1.get()


def click_5():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(5))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(5))
        g = entry1.get()

def click_6():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(6))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(6))
        g = entry1.get()





def click_7():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(7))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(7))
        g = entry1.get()


def click_8():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(8))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(8))
        g = entry1.get()


def click_9():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(9))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(9))
        g = entry1.get()


def click_0():
    if lbl['text'] != '':
        global f
        entry1.insert("end", str(0))
        f = entry1.get()
    else:
        global g
        entry1.insert("end", str(0))
        g = entry1.get()














def click_plus():
    entry1.delete(0, last='end')
    lbl['text'] = '+'

def click_minus():
    entry1.delete(0, last='end')
    lbl['text'] = '-'

def click_divide():
    entry1.delete(0, last='end')
    lbl['text'] = '/'

def click_multi():
    entry1.delete(0, last='end')
    lbl['text'] = 'X'

def clear1():
    entry1.delete(0, last='end')
    lbl['text'] = ''

def clear2(e):
    entry1.delete(0, last='end')

def close():
    root.destroy()

def calculate():
    if lbl['text'] == '+':
        entry1.delete(0, last='end')
        entry1.insert("end", str(int(f)+int(g)))
    elif lbl['text'] == '-':
        entry1.delete(0, last='end')
        entry1.insert("end", str(int(g)-int(f)))
    elif lbl['text'] == 'X':
        entry1.delete(0, last='end')
        entry1.insert("end", str(int(f)*int(g)))
    elif lbl['text'] == '/':
        entry1.delete(0, last='end')
        entry1.insert("end", str(float(g)/float(f)))









root = tkinter.Tk()
root.geometry('600x600')
root.title('Roza Calculater')
entry1 = tkinter.Entry(font="Arial 40 bold", borderwidth=3,
                       relief="sunken")
entry1.place(relheight=0.2, relwidth=0.8, relx=0, rely=0)
lbl = tkinter.Label(text='', font="Arial 40 bold", borderwidth=3,
                    relief="sunken")
lbl.place(relheight=0.2, relwidth=0.2, relx=0.8, rely=0)
num_plus = tkinter.Button(text='+', command=click_plus)
num_plus.place(relheight=0.2, relwidth=0.2, relx=0, rely=0.2)
num_minus = tkinter.Button(text='-', command=click_minus)
num_minus.place(relheight=0.2, relwidth=0.2, relx=0.2, rely=0.2)
num_multi = tkinter.Button(text='*', command=click_multi)
num_multi.place(relheight=0.2, relwidth=0.2, relx=0.4, rely=0.2)
num_dev = tkinter.Button(text='/', command=click_divide)
num_dev.place(relheight=0.2, relwidth=0.2, relx=0.6, rely=0.2)
num_7 = tkinter.Button(text='7', command=click_7)
num_7.place(relheight=0.2, relwidth=0.2, relx=0, rely=0.4)
num_8 = tkinter.Button(text='8', command=click_8)
num_8.place(relheight=0.2, relwidth=0.2, relx=0.2, rely=0.4)
num_9 = tkinter.Button(text='9', command=click_9)
num_9.place(relheight=0.2, relwidth=0.2, relx=0.4, rely=0.4)
num_zero = tkinter.Button(text='0', command=click_0)
num_zero.place(relheight=0.2, relwidth=0.2, relx=0.6, rely=0.4)
num_4 = tkinter.Button(text='4', command=click_4)
num_4.place(relheight=0.2, relwidth=0.2, relx=0, rely=0.6)
num_5 = tkinter.Button(text='5', command=click_5)
num_5.place(relheight=0.2, relwidth=0.2, relx=0.2, rely=0.6)
num_6 = tkinter.Button(text='6', command=click_6)
num_6.place(relheight=0.2, relwidth=0.2, relx=0.4, rely=0.6)
num_clear = tkinter.Button(text='Clear', command=clear1)
num_clear.place(relheight=0.2, relwidth=0.2, relx=0.6, rely=0.6)
root.bind("<Escape>", clear2)

num_1 = tkinter.Button(text='1', command=click_1)
num_1.place(relheight=0.2, relwidth=0.2, relx=0, rely=0.8)
num_2 = tkinter.Button(text='2', command=click_2)
num_2.place(relheight=0.2, relwidth=0.2, relx=0.2, rely=0.8)
num_3 = tkinter.Button(text='3', command=click_3)
num_3.place(relheight=0.2, relwidth=0.2, relx=0.4, rely=0.8)
num_Close = tkinter.Button(text='Close', command=close)
num_Close.place(relheight=0.2, relwidth=0.2, relx=0.6, rely=0.8)
calculate = tkinter.Button(text='Calculate', font="Arial 15 bold",command=calculate)
calculate.place(relheight=0.8, relwidth=0.2, relx=0.8, rely=0.2)

root.mainloop()