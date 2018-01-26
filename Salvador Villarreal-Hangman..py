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
word_bank = ["Spider man", "Hamburgers", "Pluto", "Space Invaders", "YouTube", "The Claw", "Meme lord", "High school",
             "Einstein", "Football"]
word = random.choice(word_bank)
# print(word)
