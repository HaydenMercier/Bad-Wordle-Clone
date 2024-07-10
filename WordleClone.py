import random
words = []
lettersChecked = []
lettersOut = []
lettersIn = []
guess = ""
display = ["-", "-", "-", "-", "-"]
guesses = 0
invalid = False

with open("output.txt") as file:
    for line in file:
        words.append(line.strip("\n"))
    word = str(random.choice(words))
    print(word)

    while guess != word:
        guess = input("Guess: ")
        guesses +=1
        invalid = False
        if len(guess) != len(word):
            print("Invalid Guess, please guess a 5 letter word.")
            continue
        for i in range(len(guess)):
            if not guess[i].isalpha() and invalid != True:
                print("Invalid Guess, please guess a 5 letter word")
                invalid = True
        if guess == word:
            print(f"That is correct.\nThe word was {word}.")
            print(f"It took you {guesses} guesses!")
            break
        for i in range(len(guess)):
            if guess[i] in word:
                if guess[i] == word[i]:
                    display[i] = guess[i]
                    lettersChecked.append(guess[i])
                    lettersIn.append(guess[i])
                    print(f"You found {guess[i]}!")
                else:
                    print(f"{guess[i]} is in the word...")
                    lettersChecked.append(guess[i])
                    lettersIn.append(guess[i])
            else:
                lettersChecked.append(guess[i])
                lettersOut.append(guess[i])
                print(f"{guess[i]} is not in the word...")

        print(f"You have guessed: {', '.join(sorted(set(lettersChecked))).upper()}.")
        print(f"Incorrect guesses: {', '.join(sorted(set(lettersOut))).upper()}.")
        print(f"Correct guesses: {', '.join(sorted(set(lettersIn))).upper()}.")
        print(f"Currently, the word is: {' '.join(display)}.")
