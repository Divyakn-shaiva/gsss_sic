def even_position_sum(number):
    string_number = str(number)
    even_sum = 0
    for index, digit in enumerate(string_number, start = 1):# if we need index and digit we use enumerate
        if index % 2 == 0 :   
            even_sum += int(digit)
    print("Sum of even placed digits:", even_sum)
number = int(input("Enter the number:  "))
even_position_sum(number)
