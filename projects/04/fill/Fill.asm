// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LOOP)
@24576
D=M
@BLACK
D;JGT
//set white
@24575
D=A
@R0 //i=256*32+16384
M=D
(WHITE_LOOP)
@R0
D=M
@16384//if i-16384 > 0
D=D-A
@LOOP
D;JLT //clean finish
@32768
D=A
@R0
M=M-1//i=i-1
A=M
M=D
@WHITE_LOOP
0;JMP
(BLACK)
@24576
D=A
@R0 //i=256*32+16384
M=D
(BLACK_LOOP)
@R0
@R0
D=M
@16384//if i-16384 > 0
D=D-A
@LOOP
D;JLT //clean finish
@32768
D=A
@R0
M=M-1//i=i-1
A=M
M=D
@BLACK_LOOP
0;JMP
@LOOP
0;JMP

