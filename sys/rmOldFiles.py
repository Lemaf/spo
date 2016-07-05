#!/usr/bin/env python

import os
import time
import shutil
import glob

# Sought obj, and destination obj

def findRot(findObj,numDays):
    
    oneday = 86400
    xdays = oneday*numDays
    now = time.time()

    # Directory name
    objName=glob.glob(findObj)
    for x in objName:
        timestamp = os.path.getmtime(os.path.join(x))
        if now-xdays > timestamp:
            oldFiles = os.path.join(x)
            os.remove(oldFiles)
