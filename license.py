"""
Attribution 4.0 International
Copyright (c) 2025 wayne931121
Source https://github.com/wayne931121/pyinstaller_license

Usage:
python license.py basePath targetPath

Example:
python license.py "C:\Program Files\Python313" ".\0"
"""

import find, sys, os

basePath = sys.argv[1]
targetPath = sys.argv[2]

def copy(basePath, targetPath, partten):
    for i in find.find(partten,basePath,typeMode="file"):
        newFile = i.replace("\\","-").replace("/","-").replace(":","-")+".txt"
        f  = open(os.path.join(targetPath,newFile),"wb")
        r  = open(os.path.join(basePath,i),"rb")
        f.write(r.read())
        r.close()
        f.close()
    return    

copy(basePath, targetPath, "license")
copy(basePath, targetPath, "License")
copy(basePath, targetPath, "LICENSE")
