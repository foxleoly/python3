# list all the file in a dir
#  -*- coding: utf-8 -*-
#
import os.path
from time import sleep
"""
#result = open("D:\\list.txt", "w")

RootDir = "D:\\BaiduYunDownload"
for parent, dirnames, filenames in os.walk(RootDir):
        #for dirname in dirnames:
        #    print("parent is:", parent)
        #    print("dirname is:", dirname)

        for filename in filenames:
            print("parent is:", parent)
        #    print("file name is:", filename)
            print("full name: ", os.path.join(parent, filename))
"""

RootDir = "wechat-png\\"

for fileNames in os.walk(RootDir):

    for fullPath_ in fileNames[2]:
        fullPath = RootDir+fullPath_
        print(fullPath)
        sleep(0.1)
