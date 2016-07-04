#!/usr/bin/env python

import os
import time
import shutil
import glob

# 86400 = 24 hours = 1 day
oneday = 86400
numdays = oneday*15
now = time.time()

# Sought obj, and destination obj

def olderDirName(findObj,destObj):
    # Directory name
    dirName=glob.glob(findObj)
    for x in dirName:
        timestamp = os.path.getmtime(os.path.join(x))
        if now-numdays > timestamp:
            oldFolders = os.path.join(x)
            shutil.move(oldFolders,destObj)

