 3. Multiplication Table Generator

Concepts used: Loops, input, print formatting

It generates the multiplication of a number


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
