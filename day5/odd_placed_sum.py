def odd_position_sum(number):
    string_number = str(number)
    odd_sum = 0
    for index , digit in enumerate(string_number, start = 1):
        if index % 2 != 0:
            odd_sum += int(digit)
    print("the odd digit sum is :", odd_sum)
number = int(input("Enter the number :"))
odd_position_sum(number)
