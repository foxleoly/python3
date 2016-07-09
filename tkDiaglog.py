#!/usr/local/bin/env python3
# --*-- coding: utf-8 --8--
# Author: Leo Li
from tkinter import *
# import the menu from diaLogTables.py
from diaLogTables import demos

from quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self,parent, **options)
        self.pack()
        Label(self, text="Baisc Demo").pack()
        for (key, value) in demos.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

if __name__ == '__main__':
    Demo().mainloop()
