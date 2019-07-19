# -*- coding: utf-8 -*-
# File  : print写入.py
# Date  : 2018/9/12
import sys,os
class log(object):
    def __init__(self,filename="sss.log"):
        self.terminal = sys.stdout
        self.log = open(filename,"a")
        
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        pass
    
path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = log("H:\\fc\\txt&excel的读写\\txt的读写\\sss.txt")
print(path)
print(os.path.dirname(__file__))
print("--------------")