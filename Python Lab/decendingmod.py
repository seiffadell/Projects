def sort_numbers():
    seif = []
    for i in range(5):
        num = int(input("Enter your 5 numbers: "))  # Convert input to integer
        seif.append(num)

    asend = sorted(seif)
    descesnd = sorted(seif, reverse=True)

    return asend, descesnd

asend, descesnd = sort_numbers()
print("Sorted in ascending order:", asend)
print("Sorted in descending order:", descesnd)
