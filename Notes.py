# import random
#  this is working
# print("hello world")
#
#  salvador
#
# print(5 + 3)
# print(5 - 5)
# print(7 * 9)
# print(7**2 * 9)
# print(6 / 2)
# print(3 ** 2)
#
# print  # this makes a new line. In 3.6, it looks like: print()
# print("See if you can figure this out")
# print(10 % 3)
#
# car_name = "sal car"
# car_type = "ford"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # InLine printing
# print("I have a car called %s. It's a %s." % (car_name, car_type))
#
# # Asking for input
# name = input("What is your name? ")  # In Python 3, it is just called input()
# print("Hello %s." % name)
#
# # age = input("How Old are you? ")
# # print("%s Wow. That's Old." % age)
#
# #functions
#
#
# def print_hw():
#     print("hello world")
#
#
# print_hw()
# print_hw()
# print_hw()
#
# def say_hi(name): # name is parameter
#     print("hello %s." % name)
#     print("enjoy your day.")
#
#
# say_hi("John")
#
#
# def print_age(name, age):
#     print("%s is %d years old" % (name,age))
#     age += 1  # age = age + 1
#     print("next year, they will be %d" % age)
#
#
# print_age("John", 15)
#
# def f(x):
#    return x**3 + 4 * x**2 + 7 * x - 4
#
#
# print(f(3))
# print(f(4))
# print(f(5))
#
#
# # if statements
#
# def grade_calc(percentage):
#     if percentage >=90:
#          return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage >= 50:
#         return "F"
# print(grade_calc(100))
#
#
# def happy_b day(name):
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to " + name + ",")
#     print("Happy birthday to you.")
#
# happy_b day("john")
#
#
# # Loops
#
# for num in range(10):
#     print(num)
#
# # Do not run!!!
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
#
#
# # random numbers
#
#
#
#
# """print(1 ==1)
# print(1 != 2)
# print(10 <= 15)
# print(not False)
#
# # recasting
#
# c = '1'
# print(c == 1)
# print(int(c) == 1)
# print(c == str(1))
# """

# list
the_count = [1, 2, 3, 4, 5]
shopping_list = ["noodles", "Egg rolls", "milk", "rice", "chips"]

print(shopping_list[2])

print(len(shopping_list))

# going through a list
for item in shopping_list:
    print(item)

for num in the_count:
    print(num * 2)

len(shopping_list)  # gives me the length of the list
range(3)  # gives a list of numbers 0 through 2
range(len(shopping_list))  # a list of every index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))

# turn things into a list
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
