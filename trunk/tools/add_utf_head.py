#! -*- coding:utf-8 -*-
import os

cwd = os.getcwd()
files = os.listdir(cwd)
for file in files:
    suffix = file[-2:]
    if suffix != "py":
        continue
    fh = open(file, "r")
    print file
    cont = fh.read()
    fh.close()
    newcont = "#! -*- coding:utf-8 -*-\n" + cont
    fh = open(file, "w")
    fh.write(newcont)
    fh.close()


