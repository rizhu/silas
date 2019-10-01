from fractions import gcd

class Rational:
	"""
	Class representing fractions as fractions instead of decimals
	"""
	def rational(n,d):
		"""Rational constructor"""
		g = gcd(n, d)
    	return [n//g, d//g]

	def add_rational(x, y):
    	"""The sum of rational numbers X and Y."""
    	nx, dx = numer(x), denom(x)
    	ny, dy = numer(y), denom(y)
    	return rational(nx * dy + ny * dx, dx * dy)

	def mul_rational(x, y):
    	"""The product of rational numbers X and Y."""
    	return rational(numer(x) * numer(y), denom(x) * denom(y))

	def rationals_are_equal(x, y):
    	"""True iff rational numbers X and Y are equal."""
    	return numer(x) * denom(y) == numer(y) * denom(x)

	def print_rational(x):
    	"""Print rational X."""
    	print(numer(x), "/", denom(x))
	
