@i
M = 0

(loop)
	@i
	M=M+1
	D=M
	@0
	D=M-D
	@end
	D; JLE
	
	@loop
	0; JMP
(end)

@end
0; JMP
