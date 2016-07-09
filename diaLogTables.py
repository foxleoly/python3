#!/usr/local/bin/env python3
# --*-- coding: utf-8 --8--
# Author: Leo Li
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warrning', 'You type "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead,Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card num')
}