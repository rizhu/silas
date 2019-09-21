import math

def round_to_n(x, n):
		"""
		Rounds float x to n significant figures
		"""
		if not x == 0:
			return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))
		else:
			return x

def cmd_check(check_input, return_type = str):
		"""
		Allows user to execute commands at any point

		check_input: Input to be checked
		"""
		if check_input == "exit()":
			exit()
		return check_input

def try_input_for_type(input_str, error_string, type_func = str, cond = lambda x : True, error = ValueError):
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
				return_value = type_func(cmd_check(input(input_str)))
			except error:
				print(error_string)
			else:
				if cond(return_value):
					valid = True
				else:
					print(error_string)
		return return_value