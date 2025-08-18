def pascal_triangle(number):
    for i in range(number):
        print("  " * (number - i - 1), end = "  ")
        current_row = 1
        for j in range(i + 1):
            print(current_row, end = "  ")
            current_row = current_row * (i - j) // (j + 1)
        print()
number = int(input("enter the number :  "))
pascal_triangle(number)


