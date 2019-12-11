#!/usr/bin/env python3

import argparse
from . import var_list
from . import strings
from .classes import augmented_matrix as am
"""
import argparse
import var_list
import strings
from classes import augmented_matrix as am
"""

def main_defaults(args):
	"""
	Argument parsing for main ArgumentParser
	"""
	if args.help:
		print(strings.general_help)
	elif args.listvars:
		var_list.print_all()
	elif args.delete:
		var_list.del_var(args.delete[0])
		var_list.print_all()
	elif args.clear:
		var_list.clear()
		print(strings.var_list_clear)
	elif args.show:
		temp_var = var_list.get_var(args.show)
		if temp_var:
			print(temp_var)
		del temp_var

def am_defaults(args):
	"""
	Argument parsing for augmented matrix subparser
	"""
	if args.help:
		print(strings.am_help)
	elif args.create:
		temp_am = am.AugmentedMatrix()
		if len(args.create) == 2 and (args.create[1] == "fast" or args.create[1] == "f"):
			temp_am.build(fast_build = True, human_row_nums = True)
		else:
			temp_am.build(human_row_nums = True)
		var_list.store_var(args.create[0], temp_am)
		del temp_am
	elif args.swaprows:
		if len(args.swaprows) < 3 or len(args.swaprows) > 4:
			print("Invalid number of arguments")
			return
		temp_am = var_list.get_var(args.swaprows[0])
		try:
			temp_am.swap_rows(first_row = int(args.swaprows[1]), second_row = int(args.swaprows[2]), human_row_nums = True)
			print(f"Result of swapping rows:\n{temp_am}")
		except TypeError:
			print(f"Row arguments must be integers. Got row {args.swaprows[1]} and {args.swaprows[2]}.")
			return
		if len(args.swaprows) == 4 and (args.swaprows[3] == "s" or args.swaprows[3] == "store"):
			var_list.store_var(args.swaprows[0], temp_am)
		del temp_am
	elif args.addrows:
		if len(args.addrows) < 4 or len(args.addrows) > 5:
			print("Invalid number of arguments")
			return	
		temp_am = var_list.get_var(args.addrows[0])
		try:
			temp_am.add_rows(first_row = int(args.addrows[1]), second_row = int(args.addrows[2]), store_row = int(args.addrows[3]), human_row_nums = True)
			print(f"Result of adding rows:\n{temp_am}")
		except TypeError:
			print(f"Row arguments must be integers. Got row {args.addrows[1]} ({type(args.addrows[1])}) and {args.addrows[2]} ({type(args.addrows[2])}).")
			return
		if len(args.addrows) == 5 and (args.addrows[4] == "s" or args.addrows[4] == "store"):
			var_list.store_var(args.addrows[0], temp_am)
		del temp_am
	elif args.multrow:
		if len(args.multrow) < 3 or len(args.multrow) > 4:
			print("Invalid number of arguments")
			return
		temp_am = var_list.get_var(args.multrow[0])
		try:
			temp_am.mult_row(row = int(args.multrow[1]), constant = float(args.multrow[2]), store = True, human_row_nums = True)
			print(f"Result of multiplying row by constant:\n{temp_am}")
		except TypeError:
			print(f"Row argument must be integer and constant must be decimal value. Got row {args.multrow[1]} and constant {args.multrow[2]}.")
			return
		if len(args.multrow) == 4 and (args.multrow[3] == "s" or args.multrow[3] == "store"):
			var_list.store_var(args.multrow[0], temp_am)
		del temp_am
	elif args.elim:
		temp_am = var_list.get_var(args.elim[0])
		if len(args.elim) < 2 or args.elim[1].lower() == "gaussian" or args.elim[1].lower() == "g":
			temp_am.elim_gaussian()
		elif args.elim[1].lower() == "gaussjordan" or args.elim[1].lower() == "gj":
			temp_am.elim_gauss_jordan()
		else:
			print("Final argument must be 'gaussian' [abbr. 'g'] or 'gaussjordan' [abbr. 'gj'].")
		if len(args.elim) == 3 and args.elim[2]:
			if args.elim[2] == "store" or args.elim[2] == "s":
				var_list.store_var(args.elim[0], temp_am)
			else:
				print("Optional store argument must be 'store' [abbr. 's'].")
		del temp_am



def main():
	main_parser = argparse.ArgumentParser(prog = 'silas', usage = strings.general_arg_help, add_help = False)
	main_parser.add_argument("-h", "--help", action ='store_true')
	main_parser.add_argument("-ls", "--listvars", help = strings.general_arg_help, action ='store_true')
	main_parser.add_argument("-d", "--delete", nargs = 1, metavar = "<var-name>", type = str)
	main_parser.add_argument("--clear", help = strings.general_arg_help, action ='store_true')
	main_parser.add_argument("-s", "--show", metavar = "<var-name>", type = str)
	subparsers = main_parser.add_subparsers()
	main_parser.set_defaults(func = main_defaults)

	m_parser = subparsers.add_parser('matrix', aliases = ["m"], add_help = False)
	m_parser.add_argument("-c", "--create", metavar = "<var-name>", type = str, help = "creates a matrix with variable name as <var-name>")
	m_parser.add_argument("-b", "--build", metavar = "<var-name>", type = str, help = "builds a matrix stored at <var_name>")

	am_parser = subparsers.add_parser('augmentedmatrix', aliases = ["am"], usage = strings.am_arg_help, add_help = False)
	am_parser.add_argument("-h", "--help", action ='store_true')
	am_parser.add_argument("-c", "--create", nargs = '+', metavar = "<var-name>", type = str)
	am_parser.add_argument("-sw", "--swaprows", nargs = '+', type = str)
	am_parser.add_argument("-add", "--addrows", nargs = '+', type = str)
	am_parser.add_argument("-mul", "--multrow", nargs = '+', type = str)
	am_parser.add_argument("-e", "--elim", nargs = '+', type = str)
	am_parser.set_defaults(func = am_defaults)

	args = main_parser.parse_args()
	args.func(args)

if __name__ == "__main__":
    main()

