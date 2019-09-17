import math
import numpy as np
import sys

class AugmentedMatrix:
	"""
	Class containing all functions and values involved in setup and manipulation of the augmented matrix

	coefficients: NumPy array containing coefficients of the augmented matrix
	constants:    NumPy array containing constants of augmented matrix
	"""

	np.set_printoptions(threshold=sys.maxsize)	#Forces NumPy to print entire ndarray regardless of size

	coefficients, constants = np.array([]), np.array([])

	def round_to_n(self, x, n):
		"""
		Rounds float x to n significant figures
		"""
		return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

	def __str__(self):
		""" 
		Overrides __str__ function to print the augmented matrix using print()
		"""

		str_matrix = ""
		for i in range(self.coefficients.shape[0]):
			str_matrix += f"[ "
			for j in range(self.coefficients.shape[1] + 1):
				if j < self.coefficients.shape[1]:
					if self.coefficients[i, j] == -0.0:
						str_matrix += f"{str(0.0)} "
					else:
						str_matrix += f"{str(self.round_to_n(self.coefficients[i, j], 5))} "
				else:
					if self.constants[i, 0] == -0.0:
						str_matrix += f"| {0.0} "
					else:
						str_matrix += f"| {self.round_to_n(self.constants[i, 0], 5)} "
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

	def build(self, rows = -1, columns = -1, human_row_nums = False):
		"""
		Builds the augmented matrix through a series of user queries

		rows:	       Number of rows in coefficient matrix
		columns:       Number of columns in coefficient matrix
		human_row_nums: If True, row numbers are processed starting as 1. Otherwise, they are processed as starting at 0.
		"""

		if rows == -1:
			rows = self.try_input_for_type(f"Number of rows: ", f"Number of rows must be a positive integer.", int, lambda x : x > 0)

		if columns == -1:
			columns = self.try_input_for_type(f"Number of columns (not including constants): ", f"Number of columns must be a positive integer.", int, lambda x : x > 0)

		self.constants, self.coefficients = np.zeros((rows, 1)), np.zeros((rows, columns))

		print(f"\nFirst, let's assign the constants (y-values, measured values, or the values in the vector to the right of the bar)")
		for i in range(rows):
			if human_row_nums:
				self.constants[i, 0] = self.try_input_for_type(f"Constant in row {i + 1}: ", f"Constant must be a real number.", float)
			else:
				self.constants[i, 0] = self.try_input_for_type(f"Constant in row {i}: ", f"Constant must be a real number.", float)
			print(self.constants)

		print(f"\nNow, let's assign the coefficients (x-values, unknown values, or the values in the matrix to the left of the bar)")
		for i in range(rows):
			for j in range(columns):
				if human_row_nums:
					self.coefficients[i, j] = self.try_input_for_type(f"Coefficient in row {i + 1}, column {j + 1}: ", f"Coefficient must be a real number.", float)
				else:
					self.coefficients[i, j] = self.try_input_for_type(f"Coefficient in row {i}, column {j}: ", f"Coefficient must be a real number.", float)
				print(self.coefficients)

		print(f"\n{self}")

	def get_row(self, row, human_row_nums = False):
		"""
		Returns specified row number as list

		row:            Row number to return
		human_row_nums: If True, row numbers are processed starting as 1. Otherwise, they are processed as starting at 0.
		"""

		if human_row_nums:
			return [self.coefficients[row - 1], self.constants[row - 1]]
		else:
 			return [self.coefficients[row], self.constants[row]]
 
	def swap_rows(self, first_row = -1, second_row = -1, human_row_nums = False):
		"""
		Swaps rows of augmented matrix through a series of user queries

		first_row:	    Row to swap.
		second_row:     Row to swap first_row with.
		human_row_nums: If True, row numbers are processed starting as 1. Otherwise, they are processed as starting at 0.
		"""

		if first_row == second_row:
			return

		if first_row == -1:
			first_row = self.try_input_for_type(f"First row to swap: ", f"Row number must be a positive integer.", int)

		if second_row == -1:
			second_row = self.try_input_for_type(f"Row to swap with: ", f"Row number must be a positive integer.", int)

		try:
			if human_row_nums:
				self.coefficients[[first_row - 1, second_row - 1]] = self.coefficients[[second_row - 1, first_row - 1]]
				self.constants[[first_row - 1, second_row - 1]] = self.constants[[second_row - 1, first_row - 1]]
			else:
				self.coefficients[[first_row, second_row]] = self.coefficients[[second_row, first_row]]
				self.constants[[first_row, second_row]] = self.constants[[second_row, first_row]]
		except IndexError:
			print(f"At least one of the inputted rows does not exist. Swap not executed.")

	def mult_row(self, row, constant, store = False, human_row_nums = False):
		"""
		Multiplies row by constant and either stores new row or returns the new row without changing it

		row:            Row number to multiply
		constant:       Constant to multiply row by
		store:          If True, stores multiplied row. Otherwise, returns the row.
		human_row_nums: If True, row numbers are processed starting as 1. Otherwise, they are processed as starting at 0.
		"""

		if store:
			if human_row_nums:
				self.coefficients[row - 1] = self.coefficients[row - 1] * constant
				self.constants[row - 1] = self.constants[row - 1] * constant
			else:
				self.coefficients[row] = self.coefficients[row] * constant
				self.constants[row] = self.constants[row] * constant
		else:
			return [self.coefficients[row] * constant, self.constants[row] * constant]

	def add_rows(self, first_row, second_row, store_row, human_row_nums = False):
		"""
		Adds two rows and stores result in specified row

		first_row:      First row to add
		second_row:     Second row to add
		store_row:      Row to store sum in
		human_row_nums: If True, row numbers are processed starting as 1. Otherwise, they are processed as starting at 0.
		"""

		if human_row_nums:
			self.coefficients[store_row - 1] = np.add(first_row[0], second_row[0])
			self.constants[store_row - 1] = np.add(first_row[1], second_row[1])
		else:
			self.coefficients[store_row] = np.add(first_row[0], second_row[0])
			self.constants[store_row] = np.add(first_row[1], second_row[1])

	def elim_gaussian(self):
		"""
		Row-reduces augmented matrix with Gaussian elimination
		"""

		pivot_row = 0
		for current_column in range(min(self.coefficients.shape[0], self.coefficients.shape[1])):	# Iterates only over square matrix

			# Checks if pivot row leads with 0 and swaps with a leading non-zero row if the pivot row leads with a zero
			if self.coefficients[pivot_row, current_column] == 0:
				leading_nonzero_row = pivot_row + 1
				while leading_nonzero_row < (self.coefficients.shape[0] - 1) and self.coefficients[leading_nonzero_row, current_column] == 0:	#Increments leading_nonzero_row until a non-zero value in the column is found
					leading_nonzero_row += 1
				if leading_nonzero_row < self.coefficients.shape[0] and not self.coefficients[leading_nonzero_row, current_column] == 0:		#Swaps rows only if the entire column isn't just zeros
					print(f"R_{pivot_row + 1} <-> R_{leading_nonzero_row + 1}")
					self.swap_rows(pivot_row, leading_nonzero_row)
					print(self)

			# Divides pivot_row so that the pivot element is 1
			if not self.coefficients[pivot_row, current_column] == 1 and not self.coefficients[pivot_row, current_column] == 0:
				print(f"R_{pivot_row + 1} / {self.round_to_n(self.coefficients[pivot_row, current_column], 5)} -> R_{pivot_row + 1}")
				self.mult_row(pivot_row, 1 / self.coefficients[pivot_row, current_column], True)
				print(self)

			# Executes row operations to achieve upper triangular form
			for current_row in range(pivot_row + 1, self.coefficients.shape[0]):
				if not self.coefficients[current_row, current_column] == 0:
					if np.sign(self.coefficients[pivot_row, current_column]) == np.sign(self.coefficients[current_row, current_column]):	# If the signs of the pivot element and the leading coefficient of subsequent rows are the same, subtract multiples of them
						print(f"{self.round_to_n(np.absolute(self.coefficients[current_row, current_column]), 5)}R_{pivot_row + 1} - {self.round_to_n(np.absolute(self.coefficients[pivot_row, current_column]), 5)}R_{current_row + 1} -> R_{current_row + 1}")
						self.add_rows(self.mult_row(pivot_row, self.coefficients[current_row, current_column]), self.mult_row(current_row, self.coefficients[pivot_row, current_column] * -1), current_row)
					else:	# Otherwise, add multiples of them
						print(f"{self.round_to_n(np.absolute(self.coefficients[current_row, current_column]), 5)}R_{pivot_row + 1} + {self.round_to_n(np.absolute(self.coefficients[pivot_row, current_column]), 5)}R_{current_row + 1} -> R_{current_row + 1}")
						self.add_rows(self.mult_row(pivot_row, np.absolute(self.coefficients[current_row, current_column])), self.mult_row(current_row, np.absolute(self.coefficients[pivot_row, current_column])), current_row)
					print(self)

			pivot_row += 1
		
		print("Result of Gaussian eliminiation:")
		print(self)









