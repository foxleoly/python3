#!/usr/local/bin/env python3
# --*-- coding: utf-8 --8--
# Author: Leo Li
from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(enteries):
    for entry in enteries:
        print('Input => "%s"' % entry.get())


def MakeForm(root, fields):
    entries =[]
    for filed in fields:
        row = Frame(root)
        lab = Label(row, width=5, text=filed)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)
    return entries

if __name__ == "__main__":
    root = Tk()
    ents = MakeForm(root,fields)
    root.bind('Return',(lambda event: fetch(ents)))
    Button(root, text='Fetch',
        command= (lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()

