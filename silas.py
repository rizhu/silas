import augmented_matrix as am

a = am.AugmentedMatrix()

def build(rows = -1, columns = -1):
	"""
	Calls build function from augmented_matrix
	"""

	a.build(rows, columns)

def get_row(row, human_row_nums = False):
	"""
	Calls get_row from augmented_matrix
	"""

	return a.get_row(row, human_row_nums = False)

def swap_rows(first_row = -1, second_row = -1, human_row_nums = False):
	"""
	Calls swap_rows from augmented_matrix and prints the matrix
	"""
	
	a.swap_rows(first_row, second_row, human_row_nums = False)
	print(a)

def mult_row(row, constant, store = True, human_row_nums = False):
	"""
	Calls mult_row from augmented_matrix and prints matrix
	"""

	a.mult_row(row, constant, store = store, human_row_nums = False)
	print(a)

def add_rows(first_row, second_row, store_row, human_row_nums = False):
	"""
	Calls add_rows from augmented_matrix and prints matrix
	"""

	a.add_rows(first_row, second_row, store_row, human_row_nums = False)
	print(a)

def elim_gaussian():
	"""
	Calls elim_gaussian from augmented_matrix
	"""

	a.elim_gaussian()

