#!Author: Leo Li
# Guide:
# 1.put the wechat on full screen
# 2.run this script
# import pyautogui lib
# --coding: utf-8 --
import pyautogui as pygui
from time import sleep

# input your msg here:
#word1 = pygui.prompt(text=r'输入你的消息：', title=r'消息')
# locate the 1st group on contact list:
# grp_x, grp_y = pygui.center(pygui.locateOnScreen('D:\workspace\python3\python3\wechat-png\grp0.png'))
# pygui.click(grp_x, grp_y, button='left')
# enter the group:
# ent_x, ent_y = pygui.center(pygui.locateOnScreen('D:\workspace\python3\python3\wechat-png\enter.png'))
# pygui.click(ent_x, ent_y, button='left')
test_x, test_y = pygui.center(pygui.locateOnScreen(r'D:\\workspace\\python3\\python3\\wechat-png\\amy.png'))
pygui.click(test_x, test_y, button='left')

#pygui.typewrite(word1, interval=0.2)

sleep(1)
pygui.hotkey('ctrl', 'v')
pygui.hotkey('alt', 's')
# wait 1 second
pygui.alert('Done!!')
