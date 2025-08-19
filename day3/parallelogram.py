def parallelogram(number_of_lines):
    for i in range(number_of_lines):
        print(" " * (number_of_lines - i - 1), end = " ")
        for j in range(number_of_lines):
            if i == 0 or i == number_of_lines - 1 or j == 0 or j == number_of_lines - 1:# if we remove if condition then solid parallelogram will be printed
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print() 
number_of_lines = int(input("enter the number of lines :  "))
parallelogram(number_of_lines)






