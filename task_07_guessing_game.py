import random
X = random.randint(1,10)
for i in range(5):
    number = input("Enter the number you guess:")
    if number == X:
        print("Congratulations")
        print(f"You guessed the number in {i} attempts")
    else:
        print("Game Over!!!")

        