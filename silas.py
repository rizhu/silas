import augmented_matrix as am

var_list = {
}

def parse_input(input_str: str):
	if input_str == "exit":
		exit()
	elif input_str == "help":
		print(f"Silas general commands (abbreviations indicated by 'abbr.'):")
		print(f"- exit: closes Silas")
		print(f"- listvars: displays all variables")
		return print(f"- augmentedmatrix: Augmented Matrix support. Type 'augmentedmatrix help' for more info")
	elif input_str == "listvars":
		for key in var_list:
			print(key)
		return
	try:
		parsed_cmd = input_str.split(" ")
	except AttributeError:
		return print(f"Command not recognized. Type help in order to view all commands.")
	if parsed_cmd[0] == "augmentedmatrix" or parsed_cmd[0] == "am":
		if len(parsed_cmd) == 2 and parsed_cmd[1] == "help":
			print(f"Commands for augmented_matrix (abbr. am):")
			print(f"- augmentedmatrix create <var_name>: creates an augmentedmatrix stored as <var_name>")
			print(f"- <var_name> build [rows] [right_columns] [left_columns]: builds augmentedmatrix at <var_name> with optional dimensions")
			print(f"- <var_name> fastbuild [rows] [right_columns] [left_columns]: builds augmentedmatrix at <var_name> with optional dimensions from raw input")
			return print(f"- <var-name> elim [gaussian (abbr. g)/gauss-jordan (abbr. gj)]: row-reduces augmented matrix using Gaussian or Gauss-Jordan elimination")
		elif len(parsed_cmd) == 3 and parsed_cmd[1] == "create":
			var_list.update({parsed_cmd[2] : am.AugmentedMatrix()})
			return print(f"Created augmented matrix as {parsed_cmd[2]}")
		else:
			return print("Command not recognized. Type 'augmentedmatrix help' in order to view all augmentedmatrix commands.")
	elif parsed_cmd[0] in var_list:
		if len(parsed_cmd) == 1:
			return print(var_list[parsed_cmd[0]])
		if type(var_list[parsed_cmd[0]]) == am.AugmentedMatrix:
			if len(parsed_cmd) >= 2 and parsed_cmd[1] == "build":
				if len(parsed_cmd) == 5:
					var_list[parsed_cmd[0]].build(int(parsed_cmd[2]), int(parsed_cmd[3]), int(parsed_cmd[4]), raw_input = False, human_row_nums = True)
				else:
					var_list[parsed_cmd[0]].build(rows = -1, cf_columns = -1, const_columns = -1, raw_input = False, human_row_nums = True)
			elif len(parsed_cmd) >= 2 and parsed_cmd[1] == "fastbuild":
				if len(parsed_cmd) == 5:
					var_list[parsed_cmd[0]].build(int(parsed_cmd[2]), int(parsed_cmd[3]), int(parsed_cmd[4]), raw_input = True, human_row_nums = True)
				else:
					var_list[parsed_cmd[0]].build(rows = -1, cf_columns = -1, const_columns = -1, raw_input = True, human_row_nums = True)
			elif len(parsed_cmd) >= 3 and parsed_cmd[1] == "elim":
				if parsed_cmd[2] == "gaussian" or "g":
					var_list[parsed_cmd[0]].elim_gaussian()
				elif parsed_cmd[2] == "gauss-jordan" or "gj":
					var_list[parsed_cmd[0]].elim_gauss_jordan()
			else:
				return print("Command not recognized. Type 'augmentedmatrix help' in order to view all augmentedmatrix commands.")
	else:
		return print(f"Command not recognized. Type help in order to view all commands.")



print(f"\n\nSilas is developed by Imran Khaliq, Noor Mahini, and Richard Hu and is licensed under the GNU General Public Licence.\n\n\n")
print(f"Welcome to Silas, the Somewhat Interactive Linear Algebra Software!\nType help if you're unsure how to begin!\n")

while True:
	parse_input(input(f"> "))