//screen is totally black at @0 = 8192

@SCREEN
D = A

@addr
M = D

@i
M = 0

(loop)
	@R0
	D = M
	
	@i
	M = M + 1
	D = D - M

	@end
	D;JLT
	
	@i
	D = M - 1

	@addr
	A = M + D
	M = -1
		
		

	@loop
	0;JMP
(end)

@end
0;JMP
