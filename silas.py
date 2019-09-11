import augmented_matrix as am

a = am.Augmented_Matrix()

def build(rows = -1, columns = -1):
	"""
	Calls build function from augmented_matrix
	"""

	a.build(rows, columns)

def swap_rows(first_row = -1, second_row = -1):
	"""
	Calls swap_rows from augmented matrix
	"""
	
	a.swap_rows(first_row, second_row)