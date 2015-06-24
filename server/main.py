#!/usr/bin/python
import sys
import os

path = sys.path[0]
if os.path.isdir(path) == True:
    RootPath = path

else:
    RootPath = os.path.dirname(path)

sys.path.append(RootPath+"/conf")
sys.path.append(RootPath+"/cache")
sys.path.append(RootPath+"/core")
sys.path.append(RootPath+"/net")


