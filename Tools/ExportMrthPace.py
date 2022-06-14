#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PacketGenerator

import imp
from ntpath import join
import os
import string
import math
from sys import path
from xml.etree.ElementTree import tostring

class ExportMrthPace(object):
    Len = 42.195

    def __init__(self):
        pass

    def SetRange(self, startPace, endPace, step):
        self.startPace = str(startPace)
        self.endPace = str(endPace)
        self.step = int(step)
        pass

    def SetExportFile(self, exportFile):
        self.exportFile = exportFile
        pass

    def GetNextTime(self, time):
        time = str(time)
        hour = (int)(time[0])
        min = (int)(time[1:3])
        if(min == 59):
            min = 0
            hour = hour + 1
        else:
            min = min + self.step
        if(min < 10):
            return str(hour) + "0" + str(min)
        else:
            return str(hour) + str(min)

    def CalculatePace(self, time):
        time = str(time)
        hour = (int)(time[0])
        min = (int)(time[1:3])
        totalMin = hour * 60 + min
        paceMin = math.floor(totalMin / ExportMrthPace.Len)
        paceSec = math.floor(((totalMin / ExportMrthPace.Len) - paceMin) * 60)
        paceMilli = math.floor((((totalMin / ExportMrthPace.Len) - paceMin) * 60 - paceSec) * 100)

        paceMin = str(paceMin)
        if(paceSec < 10):
            paceSec = "0" + str(paceSec)
        else:
            paceSec = str(paceSec)
        if(paceMilli < 10):
            paceMilli = "0" + str(paceMilli)
        else:
            paceMilli = str(paceMilli)
        return paceMin + "\'" + paceSec + "\"" + paceMilli

    def Export(self):
        result = ""
        current = self.startPace
        while(True):
            result = result + current + "\t" + self.CalculatePace(current) + "\n"
            if(current == str(self.endPace)):
                break
            pass
            current = self.GetNextTime(current)
        pass
        with open(self.exportFile, "w", encoding = "utf-8") as file:
            file.write(result)
    pass
    