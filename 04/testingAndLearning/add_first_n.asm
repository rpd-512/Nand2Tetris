@i
M = 0

@sum
M = 0


(loop)
	@i
	MD = M + 1
	
	@0
	D = M - D
	@end
	D; JLT
	
	@i
	D = M

	@sum
	M = M + D	

	@loop
	0; JMP
(end)

@end
0; JMP
	

