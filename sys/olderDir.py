#!/usr/bin/env python

import os
import time
import shutil

# 86400 = 24 hours = 1 day

oneday = 86400
numdays = oneday*15

now = time.time()
directory=os.path.join(".")

for r,d,f in os.walk(directory):
    for dir in d:
         timestamp = os.path.getmtime(os.path.join(r,dir))
         if now-numdays > timestamp:
			 try:
				 oldFolders = os.path.join(r,dir)
				 shutil.move(oldFolders,"backup")
			 except shutil.Error:
				 pass
