import classes.augmented_matrix as am
import os

with open("var_list.silas", "w+") as var_list:
	var_list.close()

def store_var(var):
	with open("var_list.silas", "w+") as var_list:
		var_list.write(f"{var.var_repr()}\n")
