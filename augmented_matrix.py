import helper as hp
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

	def __str__(self):
		""" 
		Overrides __str__ function
		"""

		str_matrix = ""
		longest_len = -1
		for i in range(self.coefficients.shape[0]):
			for j in range(self.coefficients.shape[1]):
				if len(str(hp.round_to_n(self.coefficients[i, j], 5))) > longest_len:
					longest_len = len(str(hp.round_to_n(self.coefficients[i, j], 5)))
			for k in range(self.constants.shape[1]):
				if len(str(hp.round_to_n(self.constants[i, k], 5))) > longest_len:
					longest_len = len(str(hp.round_to_n(self.constants[i, k], 5)))
		for i in range(self.coefficients.shape[0]):
			str_matrix += f"[ "
			for j in range(self.coefficients.shape[1]):
				if self.coefficients[i, j] == -0.0:
					str_matrix += f"{str(0.0)} "
					for a in range(longest_len - 3):
						str_matrix += f" "
				else:
					str_matrix += f"{str(hp.round_to_n(self.coefficients[i, j], 5))} "
					for a in range(longest_len - len(str(hp.round_to_n(self.coefficients[i, j], 5)))):
						str_matrix += f" "
			str_matrix += f"| "
			for k in range(self.constants.shape[1]):
				if self.constants[i, k] == -0.0:
					str_matrix += f"{0.0} "
					for a in range(longest_len - 3):
						str_matrix += f" "
				else:
					str_matrix += f"{hp.round_to_n(self.constants[i, k], 5)} "
					for a in range(longest_len - len(str(hp.round_to_n(self.constants[i, k], 5)))):
						str_matrix += f" "
			str_matrix += f"]\n"
		return str_matrix

	def __repr__(self):
		"""
		Overrides __repr__ function
		"""

		return str(self)

	def build(self, rows = -1, cf_columns = -1, const_columns = -1, raw_input = False, human_row_nums = False):
		"""
		Builds the augmented matrix through a series of user queries

		rows:	        Number of rows in coefficient matrix
		cf_columns:     Number of columns in coefficient matrix
		const_columns:  Number of columns in constant matrix
		human_row_nums: If True, row numbers are processed starting as 1. Otherwise, they are processed as starting at 0.
		"""

		if rows == -1:
			rows = hp.try_input_for_type(f"Number of rows: ", f"Number of rows must be a positive integer.", int, lambda x : x > 0)

		if cf_columns == -1:
			cf_columns = hp.try_input_for_type(f"Number of columns in the coefficient matrix: ", f"Number of columns must be a positive integer.", int, lambda x : x > 0)

		if const_columns == -1:
<<<<<<< HEAD
			const_columns = hp.try_input_for_type(f"Number of columns in the constant matrix: ", f"Number of columns must be a positive integer.", int, lambda x : x > 0)
=======
			const_columns = self.try_input_for_type(f"Number of columns in the constant matrix (set to 1 if solving a system of linear equations: ", f"Number of columns must be a positive integer.", int, lambda x : x > 0)
>>>>>>> Minor changes to prompts

		self.constants, self.coefficients = np.zeros((rows, const_columns)), np.zeros((rows, cf_columns))

		print(f"\nFirst, let's assign the constants (y-values, measured values, or the values in the matrix to the right of the bar)")
		if raw_input:
			elements = hp.build_from_raw_input(f"Input all elements of constants going left-to-right, top-to-bottom as integers or real numbers separated by spaces:\n")
			if len(elements) == rows * const_columns:
				self.constants = np.array(elements).reshape((rows, const_columns))
			else:
				print(f"Input did not match dimensions of matrix. Stopping build...")
				return False
		else:
			for i in range(rows):
				for j in range(const_columns):
					if human_row_nums:
						self.constants[i, j] = hp.try_input_for_type(f"Constant in row {i + 1}, column {j + 1}: ", f"Constant must be a real number.", float)
					else:
						self.constants[i, j] = hp.try_input_for_type(f"Constant in row {i}, column {j}: ", f"Constant must be a real number.", float)
					print(self.constants)

		print(f"\nNow, let's assign the coefficients (x-values, unknown values, or the values in the matrix to the left of the bar)")
		if raw_input:
			elements = hp.build_from_raw_input(f"Input all elements of coefficients going left-to-right, top-to-bottom as integers or real numbers separated by spaces:\n")
			if len(elements) == rows * cf_columns:
				self.coefficients = np.array(elements).reshape((rows, cf_columns))
			else:
				print(f"Input did not match dimensions of matrix. Stopping build...")
				return False
		else:
			for i in range(rows):
				for j in range(cf_columns):
					if human_row_nums:
						self.coefficients[i, j] = hp.try_input_for_type(f"Coefficient in row {i + 1}, column {j + 1}: ", f"Coefficient must be a real number.", float)
					else:
						self.coefficients[i, j] = hp.try_input_for_type(f"Coefficient in row {i}, column {j}: ", f"Coefficient must be a real number.", float)
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
			first_row = hp.try_input_for_type(f"First row to swap: ", f"Row number must be a positive integer.", int)

		if second_row == -1:
			second_row = hp.try_input_for_type(f"Row to swap with: ", f"Row number must be a positive integer.", int)

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
				print(f"R_{pivot_row + 1} / {hp.round_to_n(self.coefficients[pivot_row, current_column], 5)} -> R_{pivot_row + 1}")
				self.mult_row(pivot_row, 1 / self.coefficients[pivot_row, current_column], True)
				print(self)

			# Executes row operations to achieve upper triangular form
			for current_row in range(pivot_row + 1, self.coefficients.shape[0]):
				if not self.coefficients[current_row, current_column] == 0:
					if np.sign(self.coefficients[pivot_row, current_column]) == np.sign(self.coefficients[current_row, current_column]):	# If the signs of the pivot element and the leading coefficient of subsequent rows are the same, subtract multiples of them
						print(f"{hp.round_to_n(np.absolute(self.coefficients[current_row, current_column]), 5)}R_{pivot_row + 1} - {hp.round_to_n(np.absolute(self.coefficients[pivot_row, current_column]), 5)}R_{current_row + 1} -> R_{current_row + 1}")
						self.add_rows(self.mult_row(pivot_row, self.coefficients[current_row, current_column]), self.mult_row(current_row, self.coefficients[pivot_row, current_column] * -1), current_row)
					else:	# Otherwise, add multiples of them
						print(f"{hp.round_to_n(np.absolute(self.coefficients[current_row, current_column]), 5)}R_{pivot_row + 1} + {hp.round_to_n(np.absolute(self.coefficients[pivot_row, current_column]), 5)}R_{current_row + 1} -> R_{current_row + 1}")
						self.add_rows(self.mult_row(pivot_row, np.absolute(self.coefficients[current_row, current_column])), self.mult_row(current_row, np.absolute(self.coefficients[pivot_row, current_column])), current_row)
					print(self)

			pivot_row += 1
		
		print("Result of Gaussian eliminiation:")
		print(self)

	def elim_gauss_jordan(self):
		"""
		Row-reduces augmented matrix with Guass-Jordan elimination
		"""
		pass









