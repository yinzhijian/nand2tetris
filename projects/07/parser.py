#!/usr/bin/env python
#-*- coding:utf8 -*-
#author yintao
#date 2018-07-17 23:40:49

C_ARITHMETIC="C_ARITHMETIC"
C_PUSH="C_PUSH"
C_POP="C_POP"
C_LABEL="C_LABEL"
C_GOTO="C_GOTO"
C_IF="C_IF"
C_FUNCTION="C_FUNCTION"
C_RETURN="C_RETURN"
C_CALL="C_CALL"

class Parser:
    def __init__(self,file_name):
        with open(file_name, 'r') as fp:
            read_lines = fp.readlines()
            read_lines = [line.rstrip('\n') for line in read_lines]
        self.lines = []
        for index in range(len(read_lines)):
            read_lines[index] = read_lines[index].strip()
            read_lines[index] = read_lines[index].replace("\r", "")
            read_lines[index] = read_lines[index].split("//")[0]
            if read_lines[index] != "":
                self.lines.append(read_lines[index])
        self.current=-1
    
    def reset(self):
        self.current=-1

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
        if self.lines[self.current].startswith("push"):
            return C_PUSH
        if self.lines[self.current].startswith("pop"):
            return C_POP
        if self.lines[self.current].startswith("label"):
            return C_LABEL
        if self.lines[self.current].startswith("goto"):
            return C_GOTO
        if self.lines[self.current].startswith("if-goto"):
            return C_IF
        if self.lines[self.current].startswith("function"):
            return C_FUNCTION
        if self.lines[self.current].startswith("return"):
            return C_RETURN
        if self.lines[self.current].startswith("call"):
            return C_CALL
        return C_ARITHMETIC

    def arg1(self):
        # add,sub,etc
        if self.commandType() == C_ARITHMETIC:
            return self.lines[self.current]
        syms = self.lines[self.current].split(" ")
        for i in range(1,len(syms)):
            if syms[i] == "":
                continue
            return syms[i]
    def arg2(self):
        sym_count = 0
        syms = self.lines[self.current].split(" ")
        for i in range(1,len(syms)):
            if syms[i] == "":
                continue
            if sym_count == 1:
                return syms[i]
            sym_count += 1
