N = int(input("Enter a positive number: "))

while N <= 0:
    N = int(input("Invalid! Enter a positive number: "))

even_count = 0
odd_count = 0
total_sum = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    total_sum += i

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum:", total_sum)