// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.



(kbrdloop)
	@KBD
	D = M

	@i
	M = 0
	
	@scrnblack
	D;JGT
	
	@scrnwhite
	D;JEQ
	
	@kbrdloop
	0;JMP 

(scrnwhite)
	
	@8192
	D = A

	@i
	M = M + 1	
	D = D - M
	
	@kbrdloop
	D;JLT

	@i
	D = M-1

	@SCREEN
	A = A + D
	M = 0		

	@scrnwhite
	0;JMP


(scrnblack)
	
	@8192
	D = A

	@i
	M = M + 1	
	D = D - M
	
	@kbrdloop
	D;JLT

	@i
	D = M-1

	@SCREEN
	A = A + D
	M = -1		

	@scrnblack
	0;JMP


