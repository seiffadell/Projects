
def count_vowels(sentence):
    vowels = ["i", "I", "e", "E", "o", "O", "u", "U", "A", "a"]
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

userinput = input("Enter your sentence: ")
print("Number of vowels:", count_vowels(userinput))
