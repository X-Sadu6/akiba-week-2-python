Number = int(input("Enter a number:"))
Sum = 0
while Number:
    Digit = Number % 10
    Sum += Digit
    Number //= 10
print("The sum of digits is:", Sum)