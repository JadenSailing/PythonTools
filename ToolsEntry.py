#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PacketGenerator

import os
import configparser
from Tools import *
from Tools.ExportMrthPace import ExportMrthPace

cfg = configparser.ConfigParser()
cfg.read("Config.ini", encoding = "utf8")

print("# " + cfg.get("Global", "Comment"))
toolId = cfg.getint("Global", "Use")
print("# now use tool %d" % (toolId))
toolSection = ("Tool%d" % toolId)
comment = cfg.get(toolSection, "Comment")
print("# " + comment + "...")
print(">>>")
if(toolId == 1):
    counter = CodeLineCounter()
    dir = cfg.get(toolSection, "Dir")
    print("current dir = " + dir)
    counter.SetDir(dir)
    filter = cfg.get(toolSection, "Filter")
    counter.SetFilter(filter)
    dirCount, fileCount, lineCount = counter.Count()
    print("dirCount = %d" % (dirCount, ))
    print("fileCount = %d" % (fileCount, ))
    print("lineCount = %d" % (lineCount,))
    pass
elif(toolId == 2):
    counter = SameNameFile()
    dir = cfg.get(toolSection, "Dir")
    print("current dir = " + dir)
    counter.SetDir(dir)
    filter = cfg.get(toolSection, "Filter")
    counter.SetFilter(filter)
    dirCount, fileCount, sameSet = counter.Check()
    print("dirCount = %d" % (dirCount, ))
    print("fileCount = %d" % (fileCount, ))
    sameIndex = 1
    for file in sameSet:
        print("%d:%s" % (sameIndex, file))
        sameIndex = sameIndex + 1
    pass
elif(toolId == 3):
    exportFileName = cfg.get(toolSection, "FileName")
    exporter = ExportMrthPace()
    startPace = cfg.get(toolSection, "StartPace")
    endPace = cfg.get(toolSection, "EndPace")
    step = cfg.get(toolSection, "Step")
    exporter.SetRange(startPace, endPace, step)
    exporter.SetExportFile(exportFileName)
    exporter.Export()
    pass