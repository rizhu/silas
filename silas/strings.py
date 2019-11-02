###############################
#                             #
#     General-Use Strings     #
#                             #
###############################

about_silas = f"Silas is developed by Imran Khaliq, Noor Mahini, and Richard Hu and is licensed under the GNU General Public Licence.\n"

###############################
#                             #
#         CLI Strings         #
#							  #
###############################

general_help = f"""
Silas version 0.1.4.3.

Welome to Silas, the Somewhat Interactive Linear Algebra Software!

Silas is capable of storing and operating on variables such as matrices and augmented matrices. Silas runs on the command line and is designed to be quickly accessible.
Below are a list of general commands. Some commands also have abbreviations, indicated by 'abbr.', and each command must be prefixed by 'silas'.

augmentedmatrix [abbr. am]      augmented matrix sub-commands. Use 'silas augmentedmatrix --help' for more info

--delete [abbr. -d] <var-name>    deletes variable at <var-name> if it exists         
--clear                           removes all stored variables
--help [abbr. -h]                 opens this help menu
--listvars [abbr. -ls]            lists all stored variables and their type
--show [abbr. -s] <var-name>      prints the variable stored at <var-name>
"""
general_arg_help = f"Command not found. Type 'silas --help [abbr. -h]' for a list of general commands."
am_help = f"""
Augmented Matrix mode enables the creation of augmented matrices and many augmented matrix functions.
Below are a list of augmented matrix commands. Some commands also have abbreviations, indicated by 'abbr.', and each command must be prefixed by 'augmentedmatrix' [abbr. am].

--create [abbr. -c] <var-name> [optional] f/fast                                                     creates and builds an augmented matrix with name <var-name>
--build [abbr. -b] <var-name>                                                                        re-builds augmented matrix with name <var-name>
--swaprows [abbr. -sw] <var-name> <first-row> <second-row> [optional] store [abbr. s]                swaps row number <first-row> with row number <second-row> for <var-name>
--elim [abbr. -e] <var-name> gaussian [abbr. g]/gaussjordan [abbr. gj] [optional] store [abbr. s]    row-reduces augmented matrix at <var-name> with specified algorithm
"""
am_arg_help = f"Command not found. Type 'silas am --help [abbr. -h]' for a list of augmented matrix commands.\n"

###############################
#                             #
# Variable Management Strings #
#                             #
###############################

var_list_clear = f"All stored variables have been cleared!\n"

var_not_found = f"Variable not found.\n"
var_not_fetched = f"Unable to fetch variable.\n"

am_encoding = f"augmentedmatrix"
   
###############################
#                             #
#        Matrix Strings       #
#                             #
###############################

# Build strings
row_query = f"Number of rows: "
row_error = f"Number of rows must be a positive integer."

cf_col_query = f"Number of columns in the coefficient matrix: "
const_col_query = f"Number of columns in the constant matrix: "
col_error = f"Number of columns must be a positive integer."

assign_consts = f"\nFirst, let's assign the values in the constant matrix."
assign_cfs = f"\nNow, let's assign the coefficients."
real_num_check = f"Value must be a real number."

# Fast build strings
fast_query = f"Input all values going left-to-right, top-to-bottom as integers or real numbers separated by spaces:\n"
real_num_error = f"At least one inputted value was not a real number. Stopping build...\n"
dim_error = f"Inputted values did not match dimensions of matrix. Stopping build...\n"

# Swap strings
first_swap = f"First row to swap: "
second_swap = f"Row to swap with: "
swap_positive_int_error = f"Row number must be a positive integer.\n"
swap_no_row_error = f"At least one of the inputted rows does not exist. Swap not executed.\n"

# Elimination strings
result_gaussian = f"Result of Gaussian eliminiation:"
result_gj = f"Result of Guass-Jordan eliminiation:"
