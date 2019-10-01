import math
import numpy as np
import sys

class Matrix:
	"""
	Class containing all functions and values involved in setup and manipulation of normal matries
	"""

	np.set_printoptions(threshold=sys.maxsize)	#Forces NumPy to print entire ndarray regardless of size

	matrix = np.array([])

	def round_to_n(self, x, n):
		"""
		Rounds float x to n significant figures
		"""
		return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

	def __str__(self):
		"""
		"""
		pass

	def __repr__(self):
		"""
		"""
		pass