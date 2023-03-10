# A function that checks whether a list passed as an argument contains
# all digits from '1' to '9' without repetition.
def contains_all_digits(lst):
    return sorted(list(lst)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the Sudoku.
sudoku_rows = [ ]
for r in range(9):
    is_valid_row = False
    while not is_valid_row:
        row = input("Enter row #" + str(r + 1) + ": ")
        is_valid_row = len(row) == 9 or row.isdigit()
        if not is_valid_row:
            print("Incorrect row data - 9 digits required")
    sudoku_rows.append(row)

sudoku_is_valid = True

# Check if all rows are valid.
for r in range(9):
    if not contains_all_digits(sudoku_rows[r]):
        sudoku_is_valid = False
        break

# Check if all columns are valid.
if sudoku_is_valid:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(sudoku_rows[r][c])
        if not contains_all_digits(col):
            sudoku_is_valid = False
            break

# Check if all sub-grids (3x3) are valid.
if sudoku_is_valid:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            subgrid = ''
            # Make a string containing all digits from a sub-grid.
            for i in range(3):
                subgrid += sudoku_rows[r+i][c:c+3]
            if not contains_all_digits(list(subgrid)):
                sudoku_is_valid = False
                break

# Print the final verdict.
if sudoku_is_valid:
    print("Valid Sudoku Solution")
else:
    print("Invalid Sudoku Solution")
