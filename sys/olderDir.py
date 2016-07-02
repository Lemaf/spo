#!/usr/bin/env python

import os
import time
import shutil
import glob

# 86400 = 24 hours = 1 day
oneday = 86400
numdays = oneday*15
now = time.time()

# Directory name
dirName=glob.glob("teste*")

for x in dirName:
	timestamp = os.path.getmtime(os.path.join(x))
	if now-numdays > timestamp:
		oldFolders = os.path.join(x)
		shutil.move(oldFolders,"backup")

