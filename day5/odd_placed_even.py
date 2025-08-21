def odd_placed_even_digit_sum(number):
    string_number = str(number)
    even_sum = 0
    for index, digit in enumerate(string_number,start = 1):
        if index % 2 != 0 and int(digit) % 2 == 0:
            even_sum += int(digit)
    print("Odd placed Even digit Sum is :  ", even_sum)
number = int(input("Enter the number:  "))
odd_placed_even_digit_sum(number)