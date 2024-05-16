@i
M = 0

@R2
M = 0

(loop)
	@R1
	D = M
	
	@i
	M=M+1
	D = D - M;		

	@end
	D; JLT

	@R0
	D = M

	@R2
	M = M + D

	@loop
	0;JMP

(end)	

@end
0;JMP	
