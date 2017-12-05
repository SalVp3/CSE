import random
# 1) generate random number
# 2) take an input (number) from user
# 3) compare input to generated number
# 4) add higher and lower statements
# 5) add 5 guess

number = random.randint(0, 50)

if input == (number):
    print("Correct ")
elif input < (number):
    print("higher")
elif input > (number):
    print("lower")

guess = input(" ")
print("is the number %s?" % guess)

