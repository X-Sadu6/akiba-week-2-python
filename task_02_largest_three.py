Num1 = int(input("Enter the first number:"))
Num2 = int(input("Enter the second number:"))
Num3 = int(input("Enter the third number:"))
if Num1>Num2 and Num1>Num3:
    print("The first number is the largest:",Num1)
elif Num2>Num1 and Num2>Num3:
    print("The second number is the largest:",Num2)
elif Num3>Num1 and Num3>Num2:
    print("The third number is the largest:",Num3)
elif Num1 == Num2 and Num1>Num3:
    print("The first and second numbers are equal and the largest:",Num1)
elif Num1 == Num3 and Num1>Num2:
    print("The first and third numbers are equal and the largest:",Num1)
elif Num2 == Num3 and Num2>Num1:
    print("The second and third numbers are equal and the largest:",Num2)
elif Num1 == Num2 and Num1<Num3:
    print("The third number is the largest:",Num3)
elif Num1 == Num3 and Num1<Num2:
    print("The second number is the largest:",Num2)
elif Num2 == Num3 and Num2<Num1:
    print("The first number is the largest:",Num1)
else:
    print("All numbers are equal or there is a tie for the largest number.")