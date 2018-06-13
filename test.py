#PYTHON 3.6.3
#coding: utf8

from tkinter import *

top = Frame(); top.pack()
rotulo = Label(top, text='Rótulo Exemplo', foreground='blue')
rotulo.pack()
rotulo.configure(relief='ridge', font='Ariel 24 bold', border=5,  background='yellow')
