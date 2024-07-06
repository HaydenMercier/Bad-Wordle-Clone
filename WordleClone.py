import random
words = []
guess = ""
display = ""
with open("output.txt") as file:
    for line in file:
        words.append(line.strip("\n"))
    word = str(random.choice(words))
    print(word)
    while guess is not word:
        guess = input("Guess: ")
        if guess == word:
            print(f"Thats correct.\nThe word was {word}.")
            break
        for i in guess:
            if i not in word:
                print(f"{i} is not in {word.capitalize()}.")
                guess += "-"
            if i in word:
                print(f"{i} is in {word.capitalize()}.")
                guess += "i"
        