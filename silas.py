import classes.augmented_matrix as am
import strings
import argparse

var_list = {
}

def main():
	main_parser = argparse.ArgumentParser()
	main_parser.add_argument("-ls", "--listvars", help = "lists names of all stored variables", action ='store_true')
	subparsers = main_parser.add_subparsers(help='<sub-command> help')

	am_parser = subparsers.add_parser('augmentedmatrix', aliases = ["am"])
	am_parser.add_argument("-c", "--create", metavar = "<var-name>", type = str, help = "creates an augmented matrix with variable name as <var-name>")
	am_parser.add_argument("-b", "--build", metavar = "<var-name>", type = str, help = "builds augmented matrix stored at <var_name>")

	args = main_parser.parse_args()
	if args.listvars:
		print([key for key in var_list])
	elif args.create:
		var_list.update({args.create : am.AugmentedMatrix()})
	elif args.build:
		try:
			var_list[args.build]
		except:
			print(f"Variable name not found")

if __name__ == "__main__":
    main()

