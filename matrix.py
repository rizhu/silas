import math
import numpy as np
import sys

class Matrix:
	"""
	Class containing all functions and values involved in setup and manipulation of normal matries
	"""

	np.set_printoptions(threshold=sys.maxsize)	#Forces NumPy to print entire ndarray regardless of size

	matrix = np.array([])

	def __str__(self):
		"""
		"""
		pass

	def __repr__(self):
		"""
		"""
		pass

	def build(self, rows = -1, cf_columns = -1, const_columns = -1, human_row_nums = False):
		"""
		"""
		pass	

	def get_row(self, row, human_row_nums = False):
		"""
		"""
		pass

	def swap_rows(self, first_row = -1, second_row = -1, human_row_nums = False):
		"""
		"""
		pass

	def mult_row(self, row, constant, store = False, human_row_nums = False):
		"""
		"""
		pass

	def add_rows(self, first_row, second_row, store_row, human_row_nums = False):
		"""
		"""
		pass