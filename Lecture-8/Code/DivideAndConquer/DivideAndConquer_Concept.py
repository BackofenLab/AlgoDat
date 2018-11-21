def solve(problem):
	if n < threshold:
		return solution # solve directly
	else:
		# divide problem into subproblems
		# P1, P2, ..., Pk with k>=2
		S1 = solve(P1)
		S2 = solve(P2)
		...
		Sk = solve(Pk)

		# combine solutions
		return S1 + S2 + ... + Sk
