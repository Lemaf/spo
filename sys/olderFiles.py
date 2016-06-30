#!/usr/bin/env python
# Old files (10 days) 
# Import modules
import os
import time
 
# Define variables
xdays = 10
path  = r'.'
now   = time.time()
 
# List all files older than xdays
# print "\nList all files older than " + str(xdays) + " days"
# print "==========================" + "=" * len(str(xdays)) + "====="

for root, dirs, files in os.walk(path):
    for name in files:
        filename = os.path.join(root, name)
        
        if os.stat(filename).st_mtime < now - (xdays * 86400):
            if name.endswith("*-bkp-*"):
                print(filename)
	 
