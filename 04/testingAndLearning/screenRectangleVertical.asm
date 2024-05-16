@SCREEN
D = A

@addr
M = D

@i
M = 0

(loop)
	@0
	D = M
	
	@i
	M = M + 1
	D = D - M
	
	@end
	D;JLT

	@addr
	A = M	
	M = -1
	
	@32
	D = A
	
	@addr
	M = M + D

	@loop
	0;JMP
(end)

@end
0;JMP
