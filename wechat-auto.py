#
# Author: Leo Li
# --coding: utf-8 --
#
#
# Guide:
# 1. capture wechat grp title image in QQ browser
# 2. put the iamges to defined directory
# 3. run the script
# *********DO NOT MOVE mouse and TOUCH KEYBOARD when the SCRIPT RUNNING****************
#

import pyautogui as pygui
import json as js
import codecs
import clipboard as cpbd
import os.path
from time import sleep

"""
regarding the lib:
1. pyautogui. for control the mouse and keyboard
2. json. the message define as json format. You need paste the mesg to json file
3. codecs. the message include the Chinese char, it will be process using utf-8
4. clipboard. copy the message to clipboard. it will be paste to wechat by pyautogui
"""

# incase the script fail.
pygui.FAILSAFE = True

"""
load the json format data from file msg-json.txt.
"""

mesg = codecs.open('msg-json.txt', 'r', 'utf-8')
mesg_json = js.load(mesg)

# msg1 set to clipboard
cpbd.copy(mesg_json['msg1'])

# walk the image path in directory and generate the path.
Grp1Dir = "wechat-png\\"
for fileNames in os.walk(Grp1Dir):

    for _fullPath in fileNames[2]:
        fullPath = Grp1Dir + _fullPath
#        file_x, file_y = pygui.center(pygui.locateOnScreen(fullPath))
#        pygui.click(file_x, file_y, button='left')
#        pygui.hotkey('ctrl', 'v')
#        pygui.hotkey('enter')
        print(fullPath)
        sleep(2)

"""
# get the position
#test_x, test_y = pygui.center(pygui.locateOnScreen('..\\wechat-png\\amy.png'))
pygui.click(test_x, test_y, button='left')
pygui.hotkey('ctrl', 'v')
pygui.hotkey('enter')
"""
# wait 1 second
#sleep(1)

pygui.alert('发完了！打赏呗!')
