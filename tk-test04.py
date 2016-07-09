from tkinter import *


def greeting():
    print('Hello stdout wolrd!!....')


win = Frame()
win.pack()
Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
Label(win, text='Hello, contanter world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, fill=X)

win.mainloop()
