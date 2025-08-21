def next_bigger_number(number):
    digits = list(number)
    position = -1                    # pointing to last digit in list
    for i in range(len(digits) - 1, 0, -1): # length starts from 1
        if digits[i - 1] < digits[i]:    # checking last second digit is less than last digit
            position = i - 1
            break
    if position == -1:
        print("Not possible")
    else:
        for j in range(len(digits) - 1, position, -1):
            if digits[j] > digits[position]:
                digits[position], digits[j] = digits[j], digits[position]
                break
        digits[position + 1:] =  reversed(digits[position + 1:])
        print("".join(digits))
number = input("Enter  a  number :  ")
next_bigger_number(number)
