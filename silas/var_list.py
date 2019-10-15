"""import os
from . import strings
from .classes import augmented_matrix as am
"""
import os
import strings
from classes import augmented_matrix as am



with open("var_list.silas", "a+") as var_list:
	var_list.close()

def clear():
	"""
	Deletes all stored variables
	"""
	with open("var_list.silas", "r+") as var_list:
		var_list.truncate(0)
		var_list.close


def store_var(var_name: str, var):
	"""
	Stores a variable

	var_name: name to store variable as
	var:	  variable to store
	"""
	with open("var_list.silas", "r") as var_list:
		lines = var_list.readlines()
		var_list.close()
	with open("var_list.silas", "w") as var_list:
		for line in lines:
			if not var_name in line.strip("\n"):
				var_list.write(line)
		var_list.close()
		del lines
	with open("var_list.silas", "a+") as var_list:
		var_list.write(f"{var_name} : {var.var_repr()}\n")
		var_list.close()

def get_var(var_name: str):
	"""
	Fetches a variable

	var_name: name of variable to be fetched
	"""
	lines, var_line = "", ""
	with open("var_list.silas", "r") as var_list:
		lines = var_list.readlines()
		var_list.close()
	for line in lines:
		if var_name in line:
			var_line = line
			break
	if var_line:
		var_line = var_line.split()
		if var_line[2] == strings.am_encoding:
			var = am.AugmentedMatrix()
			var.build(var_input = var_line[3:])
			return var
		else:
			return print(strings.var_not_fetched)
	else:
		return print(strings.var_not_found)

def print_all():
	"""
	Prints name and type of all stored variables
	"""
	with open("var_list.silas", "r") as var_list:
		lines = var_list.readlines()
		var_list.close
	str_line = f"All variable names:\n"
	for line in lines:
		str_line += f"{line.split()[0]} : {line.split()[2]}\n"
	print(str_line)