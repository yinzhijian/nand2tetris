#!/usr/bin/env python
#-*- coding:utf8 -*-
#author yintao
#date 2018-07-17 23:40:49

A_COMMAND="A_COMMAND"
C_COMMAND="C_COMMAND"
L_COMMAND="L_COMMAND"

class Parser:
    def __init__(self,file_name):
        with open(file_name, 'r') as fp:
            read_lines = fp.readlines()
            read_lines = [line.rstrip('\n') for line in read_lines]
        self.lines = []
        for index in range(len(read_lines)):
            read_lines[index] = read_lines[index].replace(" ", "")
            read_lines[index] = read_lines[index].replace("\r", "")
            read_lines[index] = read_lines[index].split("//")[0]
            if read_lines[index] != "":
                self.lines.append(read_lines[index])
        self.current=-1
    
    def reset(self):
        self.current=-1

    def show(self):
        for index in range(len(self.lines)):
            print self.lines[index]

    def hasMoreCommands(self):
        i = 1
        while self.current+i < len(self.lines):
            if self.lines[self.current+i] != "":
                return True
            i = i + 1
        return False

    def advance(self):
        #print "advance",self.current
        self.current= self.current+ 1
        while self.lines[self.current] == "":
            self.current= self.current+ 1

    def commandType(self):
        #print self.lines[self.current]
        if self.lines[self.current][0] == "@":
            return A_COMMAND
        if self.lines[self.current][0] == "(":
            return L_COMMAND
        return C_COMMAND

    def symbol(self):
        sym = self.lines[self.current].replace("@","");
        sym = sym.replace("(","");
        sym = sym.replace(")","");
        return sym

    def dest(self):
        if "=" not in self.lines[self.current]:
            return ""
        return self.lines[self.current].split("=")[0]

    def comp(self):
        str1 = self.lines[self.current].split("=")[-1]
        return str1.split(";")[0]

    def jump(self):
        if ";" not in self.lines[self.current]:
            return ""
        return self.lines[self.current].split(";")[-1]

