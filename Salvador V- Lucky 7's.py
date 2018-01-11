import random
dice1 = random.randint(1, 6)
print("You rolled a %s " % dice1)
dice2 = random.randint(1, 6)
print("and you rolled a %s " % dice2)

print(dice1 + dice2)

number = 7
money = 15




if(dice1 + dice2) == number:
    money += 4
else:
    money -= 1


print("You have $%s left" % money)