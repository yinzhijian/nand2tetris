#!/usr/bin/env python
#-*- coding:utf8 -*-
#author yintao
#date 2018-07-18 17:31:32
from parser import *


class CodeWriter:
    def __init__(self,asm_file):
        self.asm_file = asm_file
        self.lines = []
        self.static_start_index = 16
        self.stack_start_index = 256
        self.heap_start_index = 2048
        self.io_start_index = 16384
        self.initStackPoint()
        self.index = 0
        self.segment_dict = {'local':'LCL',
                            'argument':'ARG',
                            'this':'THIS',
                            'that':'THAT',
                            'temp':'5',};

    def initStackPoint(self):
        self.lines.append("@"+str(self.stack_start_index))
        self.lines.append("D=A")
        self.lines.append("@SP")
        self.lines.append("M=D")

    def popToD(self):
        self.lines.append("@SP")
        self.lines.append("D=M-1")
        self.lines.append("AM=D")
        self.lines.append("D=M")
    def popToInnerRegister(self,index):
        self.popToD()
        self.lines.append("@"+index)
        self.lines.append("M=D")

    def close(self):
        with open(self.asm_file, 'w') as fp:
            fp.write('\n'.join(self.lines))
        pass
    def setFileName(self,vm_file):
        self.vm_file = vm_file
        pass
    
    def push(self):
        # data from register D
        self.lines.append("@SP")
        self.lines.append("A=M")
        self.lines.append("M=D")
        # sp += 1
        self.lines.append("@SP")
        self.lines.append("D=M+1")
        self.lines.append("M=D")
    def popValueToDAndM(self):
        self.popToInnerRegister("R13")
        self.popToInnerRegister("R14")
        self.lines.append("@R13")
        self.lines.append("D=M")
        self.lines.append("@R14")


    def writeArithmetic(self,command):
        if command == "add":
            self.popValueToDAndM()
            self.lines.append("D=D+M")
            self.push()
        elif command == "sub":
            self.popValueToDAndM()
            self.lines.append("D=M-D")
            self.push()
        elif command == "neg":
            self.popToInnerRegister("R13")
            self.lines.append("@R13")
            self.lines.append("D=-M")
            self.push()
        elif command == "and":
            self.popValueToDAndM()
            self.lines.append("D=M&D")
            self.push()
        elif command == "or":
            self.popValueToDAndM()
            self.lines.append("D=M|D")
            self.push()
        elif command == "not":
            self.popToInnerRegister("R13")
            self.lines.append("@R13")
            self.lines.append("D=!M")
            self.push()
        elif command == "eq":
            self.writeCondition("JEQ")
        elif command == "lt":
            self.writeCondition("JLT")
        elif command == "gt":
            self.writeCondition("JGT")

        pass
    def writeCondition(self,operator):
            self.popValueToDAndM()
            self.lines.append("D=M-D")
            self.lines.append("@"+operator.lower()+"_true"+str(self.index))
            self.lines.append("D;"+operator)
            self.lines.append("D=0")
            self.push()
            self.lines.append("@"+operator.lower()+"_end"+str(self.index))
            self.lines.append("0;JMP")
            self.lines.append("("+operator.lower()+"_true"+str(self.index)+")")
            self.lines.append("D=-1")
            self.push()
            self.lines.append("("+operator.lower()+"_end"+str(self.index)+")")
            self.index += 1

    def putSegmentIndexToA(self,segment,index):
        self.lines.append("@"+index)
        self.lines.append("D=A")
        self.lines.append("@"+segment)
        self.lines.append("A=M+D")
    def pushSegmentValueToStack(self,segment,index):
        self.putSegmentIndexToA(segment,index)
        self.lines.append("D=M")
        self.push()

    def writePushPop(self,command,segment,index):
        fixed = {"temp":5,"pointer":3,"static":16}
        if command == C_PUSH:
            if segment == "constant":
                self.lines.append("@"+index)
                self.lines.append("D=A")
                self.push()
            elif segment in fixed.keys():
                r = str(fixed[segment]+int(index))
                self.lines.append("@R"+r)
                self.lines.append("D=M")
                self.push()
            else:
                seg = self.segment_dict[segment]
                self.pushSegmentValueToStack(seg,index)
        elif command == C_POP:
            if segment in fixed.keys():
                r = str(fixed[segment]+int(index))
                self.popToInnerRegister("R"+r)
            else:
                seg = self.segment_dict[str(segment)]
                self.putSegmentIndexToA(seg,index)
                self.lines.append("D=A")
                self.lines.append("@R13")
                self.lines.append("M=D")
                self.popToD()
                self.lines.append("@R13")
                self.lines.append("A=M")
                self.lines.append("M=D")
            
        pass

