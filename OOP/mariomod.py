def print_right_aligned_triangle(rows):
    x = rows
    for i in range(1, rows + 1):
        print(" " * (x - 1), "*" * i)
        x -= 1

def fill_right_side_stars(rows):
    y = [" "] * rows
    x = rows - 1
    for i in range(rows):
        y[x - i] = "*"
        print("".join(y))
try:
        number_of_rows = int(input("Enter number of rows: "))
        print("\nRight-Aligned Triangle:")
        print_right_aligned_triangle(number_of_rows)
        
        print("\nFill Right Side With Stars (Step by Step):")
        fill_right_side_stars(number_of_rows)

except ValueError:
        print("Invalid input. Please enter a valid number.")
