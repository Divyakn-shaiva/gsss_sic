def second_biggest_digit(number):
    digits = sorted(set(str(number)))
    if len(digits) < 2:
        print("There is No second largest digit")
    else:
        print("The Second largest digit is : ", digits[-2])
number = input("Enter the number :")
second_biggest_digit(number)