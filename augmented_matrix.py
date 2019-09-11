import numpy as np
import sys

class Augmented_Matrix:
	"""
	Class containing all functions and values involved in setup and manipulation of the augmented matrix

	coefficients: NumPy array containing coefficients of the augmented matrix
	constants:    NumPy array containing constants of augmented matrix
	"""

	np.set_printoptions(threshold=sys.maxsize)	#Forces NumPy to print entire ndarray regardless of size

	coefficients, constants = np.array([]), np.array([])

	def __str__(self):
		""" 
		Overrides __str__ function to print the augmented matrix using print()
		"""
		
		str_matrix = ""
		for i in range(self.coefficients.shape[0]):
			str_matrix += f"[ "
			for j in range(self.coefficients.shape[1] + 1):
				if j < self.coefficients.shape[1]:
					str_matrix += f"{str(self.coefficients[i, j])} "
				else:
					str_matrix += f"| {self.constants[i, 0]} "
			str_matrix += f"]\n"
		return str_matrix

	def __repr__(self):
		"""
		Overrides __repr__ function to print the augmented matrix by calling the object
		"""

		return str(self)

	def try_input_for_type(input_str, error_string, type_func = str, error = ValueError):
		"""
		Polls for input until input is valid. Returns input.

		input_str:    String printed when polling for input
		error_string: String printed if error is caught
		type_func:    Function converting input to desired type
		error:		  Error to catch
		"""

		valid, return_value = False, None
		while not valid:
			try:
				return_value = type_func(input(input_str))
			except error:
				print(error_string)
			else:
				valid = True
		return return_value

	def build(self, rows = -1, columns = -1):
		"""
		Builds the augmented matrix through a series of user queries

		rows:	 Number of rows in coefficient matrix
		columns: Number of columns in coefficient matrix
		"""

		if rows == -1:
			valid = False
			while not valid:
				try:
					rows = int(input("Number of rows: "))
				except ValueError:
					print(f"Number of rows must be a positive integer.")
				else:
					if rows > 0:
						valid = True
					else:
						print(f"Number of rows must be a positive integer.")

		if columns == -1:
			valid = False
			while not valid:
				try:
					columns = int(input("Number of columns (not including constants): "))
				except ValueError:
					print(f"Number of columns must be a positive integer.")
				else:
					if columns > 0:
						valid = True
					else:
						print(f"Number of columns must be a positive integer.")

		self.constants, self.coefficients = np.zeros((rows, 1)), np.zeros((rows, columns))

		print(f"\nFirst, let's assign the constants (y-values, measured values, or the values in the vector to the right of the bar)")
		for i in range(rows):
			valid = False
			while not valid:
				try:
					self.constants[i, 0] = float(input(f"Constant in row {i + 1}: "))
				except ValueError:
					print(f"Constant must be a real number.")
				else:
					print(self.constants)
					valid = True

		print(f"\nNow, let's assign the coefficients (x-values, unknown values, or the values in the matrix to the left of the bar)")
		for i in range(rows):
			for j in range(columns):
				valid = False
				while not valid:
					try:
						self.coefficients[i, j] = float(input(f"Coefficient in row {i + 1}, column {j + 1}: "))
					except ValueError:
						print(f"Coefficient must be a real number.")
					else:
						print(self.coefficients)
						valid = True
		print(f"\n{self}")
 
	def swap_rows(self, first_row = -1, second_row = -1):
		"""
		Swaps rows of augmented matrix through a series of user queries

		first_row:	Row to swap.
		second_row: Row to swap first_row with.
		"""

		if first_row == -1:
			valid = False
			while not valid:
				try:
					first_row = int(input(f"First row to swap: "))
				except ValueError:
					print(f"Row number must be a positive integer.")
				else:
					if first_row > 0:
						valid = True
					else:
						print(f"Row number must be a positive integer.")

		if second_row == -1:
			valid = False
			while not valid:
				try:
					second_row = int(input(f"Row to swap with: "))
				except ValueError:
					print(f"Row number must be a positive integer.")
				else:
					if second_row > 0:
						valid = True
					else:
						print(f"Row number must be a positive integer.")

		self.coefficients[[first_row - 1, second_row - 1]] = self.coefficients[[second_row - 1, first_row - 1]]
		self.constants[[first_row - 1, second_row - 1]] = self.constants[[second_row - 1, first_row - 1]]

		print(self)


