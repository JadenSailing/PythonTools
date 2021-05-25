#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PacketGenerator

from ntpath import join
import os
from sys import path

class CodeLineCounter(object):
    def __init__(self):
        pass

    def SetDir(self, dir):
        self.dir = dir
        pass

    def SetFilter(self, filter):
        pass

    def GetFileLineCount(self, path):
        with open(path) as f:
            return len(f.readlines())

    def DoCount(self, dir):
        files = os.listdir(dir)
        if len(files) == 0:
            return
        for f in files:
            fPath = os.path.join(dir, f)
            if(os.path.isfile(fPath)):
                self.fileCount += 1
                self.lineCount += self.GetFileLineCount(fPath)
                pass
            else:
                self.dirCount += 1
                self.DoCount(fPath)
        pass

    def Count(self):
        self.dirCount = 0
        self.fileCount = 0
        self.lineCount = 0
        if(self.dir == None):
            print("dir is none")
            return 0, 0, 0
        if(not os.path.exists(self.dir)):
            print("dir not exist!")
            return 0, 0, 0
        self.DoCount(self.dir)
        return self.dirCount, self.fileCount, self.lineCount
    pass
    