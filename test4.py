from tkinter import *
top = Frame(); top.pack(fill='both',expand=True)
a = Label(top, text='A'); a.pack(side='left', expand=True, fill='y')
b = Label(top, text='B'); b.pack(side='bottom', expand=True, fill='both')
c = Label(top, text='C'); c.pack(side='right')
d = Label(top, text='D'); d.pack(side='top')
for w in (a,b,c,d):
  w.configure(relief='groove', border=10, font='Times 24 bold')
top.mainloop()
