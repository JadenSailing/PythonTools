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
        self.filter = filter
        self.filterArr = str.split(self.filter, ",")
        pass

    def IsValidFile(self, path):
        if(self.filter == None or self.filter == "" or self.filter == "*.*"):
            return True
        for filter in self.filterArr:
            if(str.find(path, filter) > -1):
                return True
        return False

    def GetFileLineCount(self, path):
        with open(path,'rb') as f:
            count = 0
            while True:
                data = f.read(0x400000)
                if not data:
                    break
                count += data.count(b'\n')
            return count

    def DoCount(self, dir):
        files = os.listdir(dir)
        if len(files) == 0:
            return
        for f in files:
            fPath = os.path.join(dir, f)
            if(os.path.isfile(fPath)):
                if(self.IsValidFile(f)):
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
    