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

	def cmd_check(null, check_input, return_type = str):
		"""
		Allows user to execute commands at any point

		null: Catches return of print() statement in input()
		"""
		if check_input == "exit()":
			exit()
		return check_input

	def try_input_for_type(self, input_str, error_string, type_func = str, cond = lambda x : True, error = ValueError):
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
				return_value = type_func(self.cmd_check(input(input_str)))
			except error:
				print(error_string)
			else:
				if cond(return_value):
					valid = True
				else:
					print(error_string)
		return return_value

	def build(self, rows = -1, columns = -1):
		"""
		Builds the augmented matrix through a series of user queries

		rows:	 Number of rows in coefficient matrix
		columns: Number of columns in coefficient matrix
		"""

		if rows == -1:
			rows = self.try_input_for_type(f"Number of rows: ", f"Number of rows must be a positive integer.", int, lambda x : x > 0)

		if columns == -1:
			columns = self.try_input_for_type(f"Number of columns (not including constants): ", f"Number of columns must be a positive integer.", int, lambda x : x > 0)

		self.constants, self.coefficients = np.zeros((rows, 1)), np.zeros((rows, columns))

		print(f"\nFirst, let's assign the constants (y-values, measured values, or the values in the vector to the right of the bar)")
		for i in range(rows):
			self.constants[i, 0] = self.try_input_for_type(f"Constant in row {i + 1}: ", f"Constant must be a real number.", float)
			print(self.constants)

		print(f"\nNow, let's assign the coefficients (x-values, unknown values, or the values in the matrix to the left of the bar)")
		for i in range(rows):
			for j in range(columns):
				self.coefficients[i, j] = self.try_input_for_type(f"Coefficient in row {i + 1}, column {j + 1}: ", f"Coefficient must be a real number.", float)
				print(self.coefficients)

		print(f"\n{self}")
 
	def swap_rows(self, first_row = -1, second_row = -1):
		"""
		Swaps rows of augmented matrix through a series of user queries

		first_row:	Row to swap.
		second_row: Row to swap first_row with.
		"""

		if first_row == -1:
			first_row = self.try_input_for_type(f"First row to swap: ", f"Row number must be a positive integer.", int)

		if second_row == -1:
			second_row = self.try_input_for_type(f"Row to swap with: ", f"Row number must be a positive integer.", int)

		try:
			self.coefficients[[first_row - 1, second_row - 1]] = self.coefficients[[second_row - 1, first_row - 1]]
			self.constants[[first_row - 1, second_row - 1]] = self.constants[[second_row - 1, first_row - 1]]
		except IndexError:
			print(f"At least one of the inputted rows does not exist. Swap not executed.")

		print(self)

	def mult_row(self, row, constant):
		"""
		Multiplies row by constant and returns row number

		row:      Row number to multiply
		constant: Constant to multiply row by
		"""
		
		self.coefficients[row - 1] = self.coefficients[row - 1] * constant
		self.constants[row - 1] = self.constants[row - 1] * constant
		return row

	def add_rows(self, first_row, second_row, store_row):
		"""
		Adds two rows and stores result in specified row

		first_row:  First row to add
		second_row: Second row to add
		store_row:  Row to store sum in
		"""

		self.coefficients[store_row - 1] = self.coefficients[first_row - 1] + self.coefficients[second_row - 1]
		self.constants[store_row - 1] = self.constants[first_row - 1] + self.constants[second_row - 1]




