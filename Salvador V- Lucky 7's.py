import random
number = 7
money = 15
rounds = 0
highest_money = 15

while money > 0:

    dice1 = random.randint(1, 6)
    print("You rolled a %s " % dice1)
    dice2 = random.randint(1, 6)
    print("and you rolled a %s " % dice2)
    total = dice1 + dice2
    if total == number:
        money += 4
    else:
        money -= 1
    print(total)
    print("You have $%s left" % money)

    rounds += 1
    if money == 0:
        print("You've played %s rounds" % rounds)
