def rhombus(number_of_lines):
    total_rows = 2 * number_of_lines - 1
    for i in range(total_rows):
        if i < number_of_lines:
            row = i
        else:
            row = total_rows - i - 1
        print(" " * (number_of_lines - row - 1), end = "")
        for j in range(row + 1):
            if j == 0 or j == row:    # if this condition and else part is removed then it gives solid rhombus
                print(" *", end = "")
            else:
                print("  ", end = "")
        print()
number_of_lines = int(input("Enter number of lines: "))
rhombus(number_of_lines)