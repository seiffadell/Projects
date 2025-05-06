vowels=["i","I","e","E","o","O","u","U","A","a"]
vowelcheck=input("enter your sentence :")
no=0
for i in range(len(vowelcheck)):
    char=vowelcheck[i]
    if char in vowels:
        no=+1
print("no of vowels",no)
