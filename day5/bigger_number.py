#accept a number from the user and find the next possible smallest number which is bigger than the given number having all the digits of the given number
def next_bigger_number(num):
    digits = list(str(num))  # convert number to list of characters
    
    # Step 1: Find the rightmost digit that is smaller than the digit next to it
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    if i == -1:  # digits are in descending order, no bigger permutation
        return "Not possible"
    
    # Step 2: Find the smallest digit on right side of i that is greater than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Step 3: Swap
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Reverse the digits after position i
    digits[i + 1:] = reversed(digits[i + 1:])
    
    return int("".join(digits))
number = int(input("Enter the number: "))
print("Next bigger number:", next_bigger_number(number))
