#!/usr/bin/env python

# Default modules

import os
import argparse
import sys
import time
import glob

# SPO modules
sys.path.append("sys/")
sys.path.append("docs")

from findObj import *
from rmOldFiles import *
from h import *


class orgFolders(object):
    """docstring for orgFolders"""

    # Verify root request
    os.system(". sys/sposudo")

    def __init__(self,arg,argv):
        super(orgFolders, self).__init__()
        self.arg = arg
        self.argv = argv

        dirlist = [self.arg,self.argv]

        # Check if directory exists
        for dirnames in dirlist:
            if not os.path.exists(dirnames):
                # if not, mkdir backp and releases directories
                os.makedirs(dirnames)


    def findOldFolders(self):
        """Find old directories and move"""
        findRot("sicar-bkp*","backup",15)
       

    def findOldFiles(self):
        """docstring for findOldFiles"""
        findRot("*.tar.gz","releases",15)

    def findOldestFiles(self):
        """Find and remove oldest files"""
        findRot()


#Called
mkObj1 = orgFolders("backup","releases")
mkObj1.findOldFolders()
mkObj1.findOldFiles()
# makeFolders.findFiles("car")
