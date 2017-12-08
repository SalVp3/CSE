import random
# 1) generate random number
# 2) take an input (number) from user
# 3) compare input to generated number
# 4) add higher and lower statements
# 5) add 5 guess

number = random.randint(1, 50)

# print(number)


guess = int(input(" "))

print("is the number %s?" % guess)


if guess == number:
    print("Correct ")

elif guess < number:
    print("higher")

elif guess > number:
    print("lower")

