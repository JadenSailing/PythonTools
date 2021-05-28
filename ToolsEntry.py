#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PacketGenerator

import os
import configparser
from Tools import *

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
pass