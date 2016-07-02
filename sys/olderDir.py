#!/usr/bin/env python

import os
import time
import shutil

numdays = 86400*7
now = time.time()
directory=os.path.join(".")

for r,d,f in os.walk(directory):
    for dir in d:
         timestamp = os.path.getmtime(os.path.join(r,dir))
         if now-numdays > timestamp:
             try:
                  print "removing ",os.path.join(r,dir)
                  # shutil.rmtree(os.path.join(r,dir))  #uncomment to use
             except Exception,e:
                  print e
                  pass
             else: 
                  print "some message for success"
