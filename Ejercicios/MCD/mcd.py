def mcd(n1, n2):
	if n1 == n2:
		return n1
	if n1 > n2:
		return mcd(n1 - n2, n2)
	return mcd(n1, n2 - n1)
