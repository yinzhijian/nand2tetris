#!/usr/bin/env python
#-*- coding:utf8 -*-
#author yintao
#date 2018-07-18 00:18:09

class Code:
    def __init__(self):
        pass
    def dest(self,mnemonic):
        if mnemonic == "":
            return '000'
        if mnemonic == "M":
            return '001'
        if mnemonic == "D":
            return '010'
        if mnemonic == "MD":
            return '011'
        if mnemonic == "A":
            return '100'
        if mnemonic == "AM":
            return '101'
        if mnemonic == "AD":
            return '110'
        if mnemonic == "AMD":
            return '111'
        pass

    def comp(self,mnemonic):
        dict = {'0': '0101010',
                '1': '0111111',
                '-1': '0111010',
                'D': '0001100',
                'A': '0110000',
                '!D': '0001101',
                '!A': '0110001',
                '-D': '0001111',
                '-A': '0110011',
                'D+1': '0011111',
                'A+1': '0110111',
                'D-1': '0001110',
                'A-1': '0110010',
                'D+A': '0000010',
                'D-A': '0010011',
                'A-D': '0000111',
                'D&A': '0000000',
                'D|A': '0010101',
                'M': '1110000',
                '!M': '1110001',
                '-M': '1110011',
                'M+1': '1110111',
                'M-1': '1110010',
                'D+M': '1000010',
                'D-M': '1010011',
                'M-D': '1000111',
                'D&M': '1000000',
                'D|M': '1010101',
                };
        return dict[mnemonic]

    def jump(self,mnemonic):
        if mnemonic == "":
            return '000'
        if mnemonic == "JGT":
            return '001'
        if mnemonic == "JEQ":
            return '010'
        if mnemonic == "JGE":
            return '011'
        if mnemonic == "JLT":
            return '100'
        if mnemonic == "JNE":
            return '101'
        if mnemonic == "JLE":
            return '110'
        if mnemonic == "JMP":
            return '111'
        pass
