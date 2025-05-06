def print_multiplication_table(x):
    for i in range(1, x + 1):
        for b in range(1, i + 1):
            print(f"{i}*{b}= {i*b}")
try:
        number = int(input("Enter your number: "))
        print_multiplication_table(number)
except ValueError:
        print("Please enter a valid integer number.")
