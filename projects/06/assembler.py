#!/usr/bin/env python
#-*- coding:utf8 -*-
#author yintao
#date 2018-07-17 23:40:11
from parser import *
from code import *
import sys
import os

class Assembler:
    def __init__(self,file_name):
        portion = os.path.splitext(file_name)
        self.hack_file = portion[0]+".hack"
        self.p = Parser(file_name)
        self.code = Code();
        self.symbol_table = dict()
        self.symbol_table['SP'] = 0
        self.symbol_table['LCL'] = 1
        self.symbol_table['ARG'] = 2
        self.symbol_table['THIS'] = 3
        self.symbol_table['THAT'] = 4
        for i in range(0,16):
            self.symbol_table['R' + str(i)] = i
        self.symbol_table['SCREEN'] = 0x4000
        self.symbol_table['KBD'] = 0x6000
        self.variable_address = 16
        #print self.symbol_table

    def firstPass(self):
        count = -1
        while self.p.hasMoreCommands():
            self.p.advance()
            type = self.p.commandType()
            if type == A_COMMAND:
                count = count + 1
            elif type == C_COMMAND:
                count = count + 1
            elif type == L_COMMAND:
                self.symbol_table[self.p.symbol()] = count + 1
        self.p.reset()

    def secondPass(self):
        binarys = []
        while self.p.hasMoreCommands():
            self.p.advance()
            type = self.p.commandType()
            if type == A_COMMAND:
                symbol = 0
                if self.p.symbol().isdigit():
                    symbol = int(self.p.symbol())
                else:
                    if self.p.symbol() in self.symbol_table:
                        symbol = self.symbol_table[self.p.symbol()]
                    else:
                        self.symbol_table[self.p.symbol()] = self.variable_address
                        symbol = self.symbol_table[self.p.symbol()]
                        self.variable_address += 1

                binarys.append("{0:0=16b}".format(symbol))
                pass
            elif type == C_COMMAND:
                #print self.code.comp(self.p.comp()),self.code.dest(self.p.dest()),self.code.jump(self.p.jump())
                #print self.p.comp(),self.p.dest(),self.p.jump()
                binarys.append("111"+self.code.comp(self.p.comp())+self.code.dest(self.p.dest())+self.code.jump(self.p.jump()))
                pass
            elif type == L_COMMAND:
                pass

        with open(self.hack_file, 'w') as fp:
            fp.write('\n'.join(binarys))

    def assembler(self):
        self.firstPass()
        self.secondPass()
        pass

if __name__=="__main__":
    if len(sys.argv) != 2:
        print 'should input file name'
        exit() 
    file_name = sys.argv[1]
    a = Assembler(file_name)
    a.assembler()


