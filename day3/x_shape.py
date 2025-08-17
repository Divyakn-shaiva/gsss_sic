def x_shape (number_of_lines) :
    for i in range(number_of_lines):
        for j in range (number_of_lines):
            if j == i or j == number_of_lines - i - 1:
                print("*" , end = " ")
            else:
                print(" " , end = " ")
        print()
x_shape(12)
