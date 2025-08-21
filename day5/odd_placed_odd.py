def odd_placed_odd_digit_sum(number):
    string_number = str(number)
    odd_sum = 0
    for index, digit in enumerate(string_number, start = 1):
        if index % 2 != 0 and int(digit) % 2 != 0:
            odd_sum += int(digit)
    print("The Odd placed odd digit sum is :", odd_sum)
number = int(input("Enter the number : "))
odd_placed_odd_digit_sum(number)