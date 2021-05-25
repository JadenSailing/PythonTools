#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PacketGenerator

import os
import configparser
from Tools import *

cfg = configparser.ConfigParser()
cfg.read("Config.ini", encoding = "utf8")

print(cfg.get("Global", "Comment"))
toolId = cfg.getint("Global", "Use")
print("now use id = %d" % (toolId))
toolSection = ("Tool%d" % toolId)
comment = cfg.get(toolSection, "Comment")
print(comment + "...")
if(toolId == 1):
    counter = CodeLineCounter()
    dir = cfg.get(toolSection, "Dir")
    print("current dir = " + dir)
    counter.SetDir(dir)
    dirCount, fileCount, lineCount = counter.Count()
    print("dirCount = %d, fileCount = %d, lineCount = %d" % (dirCount, fileCount, lineCount))
    pass
pass