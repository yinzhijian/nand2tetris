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
(START)
//loop
@SCREEN
D=A
@R0
M=D//i=16384
(LOOP)
@R0
D=M
@24575//if i-24575>= 0
D=D-A
@START
D;JGT //finish one round
@24576
D=M
@BLACK
D;JGT
//white
@R0
A=M
M=0
@INC
0;JMP
(BLACK)
@R0
A=M
M=-1
(INC)
@R0
M=M+1//i=i+1
@LOOP
0;JMP
