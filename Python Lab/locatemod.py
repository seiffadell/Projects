def find_i_in_sentence(sentence):
    x = "i"
    positions = []
    for i in range(len(sentence)):
        if sentence[i] == x:
            positions.append(i)
    return positions

sentence = input("Enter your sentence: ")
positions = find_i_in_sentence(sentence)
if positions:
        for pos in positions:
            print(f"'i' found in position: {pos}")
else:
        print("No 'i' found in the sentence.")
