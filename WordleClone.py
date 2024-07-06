import random
words = []
lettersChecked = []
lettersOut = []
lettersIn = []
guess = ""
display = ""
guesses = 0
with open("output.txt") as file:
    for line in file:
        words.append(line.strip("\n"))
    word = str(random.choice(words))
    print(word)
    while guess is not word:
        guess = input("Guess: ")
        guesses +=1
        if guess == word:
            print(f"That is correct.\nThe word was {word}.")
            print(f"It took you {guesses} guesses!")
            break
        for i in guess:
            if word.index(i) == guess.index(i):
                display += i
            elif i not in word:
                print(f"{i} is not in {word.capitalize()}.")
                display += "-"
                lettersOut.append(i)
                lettersChecked.append(i)
            elif i in word:
                print(f"{i} is in {word.capitalize()}.")
                lettersIn.append(i)
                lettersChecked.append(i)
                display += "-"
        print(display)
        print(f"You have guessed: {', '.join(lettersChecked).upper()}.")
        print(f"Incorrect guesses: {', '.join(lettersOut)}.")
        print(f"Correct guesses: {','.join(lettersIn)}.")
        print(f"Currently, the word is: {display}.")