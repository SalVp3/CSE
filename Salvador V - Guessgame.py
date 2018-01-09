import random
# 1) generate random number
# 2) take an input (number) from user
# 3) compare input to generated number
# 4) add higher and lower statements
# 5) add 5 guess

number = random.randint(1, 50)

print('''
Hello welcome to guess game.
 You have 5 guesses to find the number I have thought.
  The number is 1 to 50
'''
    )
# print(number)

guesses = 5
guess = 0




while guesses > 0 and guess != number:
    guess = int(input(" "))

    if guess == number:
        print("Correct ")
        guesses = -1

    elif guess < number:
        print("higher")
        guesses -= 1

    elif guess > number:
        print("lower")
        guesses -= 1

if guesses == 0:
    print("You lost")
    print("*GAME OVER")

if guesses == -1:
    print("*YOU WIN*")