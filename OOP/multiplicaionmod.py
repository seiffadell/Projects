def generate_multiplication_lists(x):
    result = []
    for i in range(1, x + 1):
        temp = []
        for b in range(1, i + 1):
            temp.append(i * b)
        result.append(temp)
    return result
try:
        x = int(input("Enter your number: "))
        lists = generate_multiplication_lists(x)
        for sublist in lists:
            print(sublist)
except ValueError:
        print("Please enter a valid integer number.")