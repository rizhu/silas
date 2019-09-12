import augmented_matrix as am

a = am.Augmented_Matrix()

def build(rows = -1, columns = -1):
	"""
	Calls build function from augmented_matrix
	"""

	a.build(rows, columns)

def swap_rows(first_row = -1, second_row = -1):
	"""
	Calls swap_rows from augmented_matrix
	"""
	
	a.swap_rows(first_row, second_row)

def mult_row(row, constant):
	"""
	Calls mult_row_by_constant from augmented_matrix
	"""

	return a.mult_row(row, constant)

def add_rows(first_row, second_row, store_row):
	"""
	Calls add_rows from augmented_matrix
	"""

	a.add_rows(first_row, second_row, store_row)