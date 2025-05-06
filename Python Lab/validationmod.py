def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            print("Valid name.")
            return name
        else:
            print("Not valid! Please enter your name again.")
user_name = get_valid_name()
print("Welcome,", user_name)