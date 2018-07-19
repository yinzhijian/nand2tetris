#!/usr/bin/env python
#-*- coding:utf8 -*-
#author yintao
#date 2018-07-18 18:32:27
from parser import *
from code_writer import *
import sys
import os

class Translator:
    def __init__(self,path):
        self.files = []
        if os.path.isdir(path):
            self.hack_file = path+os.sep+path.strip(os.sep).split(os.sep)[-1] + ".asm"
            files= os.listdir(path) #得到文件夹下的所有文件名称
            for file in files:
                if not os.path.isdir(path+os.sep+file):
                    portion = os.path.splitext(file)
                    if portion[-1] == ".vm":
                        self.files.append(path+os.sep+file)
        else:
            self.files.append(path)
            portion = os.path.splitext(path)
            self.hack_file = portion[0]+".asm"

    def translator(self):
        print self.hack_file
        writer = CodeWriter(self.hack_file)
        for file in self.files:
            print file
            p = Parser(file)
            writer.setFileName(file)
            while p.hasMoreCommands():
                p.advance()
                type = p.commandType()
                if type == C_PUSH:
                    writer.writePushPop(type,p.arg1(),p.arg2())
                elif type == C_POP:
                    writer.writePushPop(type,p.arg1(),p.arg2())
                elif type == C_ARITHMETIC:
                    writer.writeArithmetic(p.arg1())
        writer.close()

if __name__=="__main__":
    if len(sys.argv) != 2:
        print 'should input file name'
        exit() 
    path = sys.argv[1]
    t = Translator(path)
    t.translator()

