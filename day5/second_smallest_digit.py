def second_smallest_digit(number):
    digits = sorted(set(str(number)))     # set removes duplicate elements and only unique digits are kept and sorted() creates a  new list in ascending order
    if len(digits) < 2:
        print("There is No 2nd smallest digit ")
    else:
        print("The 2nd smallest digit is:", digits[1]) # if we need smallest digit then we give digits[0] .This takes 0th index value from list
number = int(input("Enter the number: "))
second_smallest_digit(number)