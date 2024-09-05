import random
words = []
lettersChecked = []
lettersOut = []
lettersIn = []
display = ["-"] * 5
guesses = 0

def get_word():
    with open("output.txt") as file:
        for line in file:
            words.append(line.strip("\n"))
        word = str(random.choice(words))
    return word
def validate_guess(guess):
    guess = str(guess).lower()
    if len(guess) != 5:
        return "invalid"
    else:
        for i in range(len(guess)):
                if not guess[i].isalpha():
                    return "invalid"
        return "valid"
def check_guess(guess, word, guesses):
    guess = str(guess)
    word = str(word)
    guesses = int(guesses)
    global display
    global lettersChecked
    global lettersIn
    global lettersOut
    message = ""
    if guess == word:
        message = "That is correct.\nThe word was " + word +".\nIt took you " + str(guesses) + " guesses."
    else:
        for i in range(len(guess)):
            if guess[i] in word:
                if guess[i] == word[i]:
                    display[i] = guess[i]
                    lettersChecked.append(guess[i])
                    lettersIn.append(guess[i])
                    message += "You found " + guess[i] +".\n"
                else:
                    message += guess[i] +" is in the word...\n"
                    lettersChecked.append(guess[i])
                    lettersIn.append(guess[i])
            else:
                lettersChecked.append(guess[i])
                lettersOut.append(guess[i])
                message += guess[i] +" is not in the word...\n"
        message += f"You have guessed: {', '.join(sorted(set(lettersChecked))).upper()}.\nIncorrect guesses: {', '.join(sorted(set(lettersOut))).upper()}\nCorrect guesses: {', '.join(sorted(set(lettersIn))).upper()}\nCurrently, the word is: {' '.join(display)}."
        
    return message, display
word = get_word()
while True:
    guess = input("Guess: ")
    if validate_guess(guess) == "invalid":
        print("Invalid Guess, please guess a 5 letter word.")
        continue
    guesses += 1
    result, display = check_guess(guess, word, guesses)
    print(result)
    if guess == word:
        break