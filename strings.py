###############################
#                             #
#     General-Use Strings     #
#                             #
###############################

about_silas = f"Silas is developed by Imran Khaliq, Noor Mahini, and Richard Hu and is licensed under the GNU General Public Licence."

###############################
#                             #
#         CLI Strings         #
#							  #
###############################

general_help = f""
am_help = f"- augmentedmatrix create <var_name>: creates an augmentedmatrix stored as <var_name>"
   
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

assign_consts = f"\nFirst, let's assign the values in the constant matrix"
assign_cfs = f"\nNow, let's assign the coefficients"
real_num_check = f"Value must be a real number."

# Fast build strings
fast_query = f"Input all values going left-to-right, top-to-bottom as integers or real numbers separated by spaces:\n"
real_num_error = f"At least one inputted value was not a real number. Stopping build..."
dim_error = f"Inputted values did not match dimensions of matrix. Stopping build..."

# Swap strings
first_swap = f"First row to swap: "
second_swap = f"Row to swap with: "
swap_positive_int_error = f"Row number must be a positive integer."
swap_no_row_error = f"At least one of the inputted rows does not exist. Swap not executed."

# Elimination strings
result_gaussian = f"Result of Gaussian eliminiation:"
result_gj = f"Result of Guass-Jordan eliminiation:"
