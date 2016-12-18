def solve(problem):
	if n < threshold:
		# solve directly
		return solution
	else:
		# divide problem into subproblems
		# P1, P2, ..., Pk with k>=2
		S1 = solve(P1)
		S2 = solve(P2)
		...
		Sk = solve(Pk)
		
		# combine solutions
		return S1 + S2 + ... + Sk
