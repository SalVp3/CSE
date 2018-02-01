import random
"""
A general guide for hangman
1.Make a word bank - 10 items
2.Pick an random item from the list
3.Add a guess to the list of letters guessed
4.Reveal letters already guessed
5.Create the win condition
"""

count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word_bank = ["spider man", "hamburgers", "pluto", "space invaders", "youtube", "the claw", "meme lord", "high school",
             "einstein", "football"]
word = random.choice(word_bank)
# print(word)
letters_guessed = [' ']
guess = ""
guess_left = 10
win = False
while guess != "end" and not win:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))
    if output == list(word):
        print("You win")
        win = True
        continue
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print("letters guess, %s" % letters_guessed)

    if guess not in word:
        guess_left -= 1
    print("you have %s guesses left " % guess_left)
    if guess_left == 0:
        win = True
        print("The word was '%s'. You lose" % word)
