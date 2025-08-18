#check if the number is perfect square or not
import math
def is_perfect_square(number):
    if number < 0:
        return False
    root = math.sqrt(number)
    if root * root == number:
        print(number,"is a perfect square" )
    else:
         print(number,"is  not a perfect square" )

number = int(input("enter a number:  "))
is_perfect_square(number)
