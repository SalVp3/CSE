# # this is working
# print("hello world")
#
# # salvador
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
# age = input("How Old are you? ")
# print("%s Wow. Thats Old." % age)

#functions


def print_hw():
    print("hello world")


print_hw()
print_hw()
print_hw()

def say_hi(name): # name is parameter
    print("hello %s." % name)
    print("enjoy your day.")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old" % (name,age))
    age += 1  # age = age + 1
    print("next year, they will be %d" % age)


print_age("john", 15)

def f(x):
   return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))


# if statements

def grade_calc(percentage):
    if percentage >=90:
         return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "F"
print(grade_calc(100))
