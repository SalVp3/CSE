def reverse_order(first_name, last_name):
    # print("%s, %s" % (last_name, first_name))
    print(last_name + " " + first_name) # concatenation

def reverse_order():
    first_name = input("first name")
    last_name = input("last name")
    print("%s, %s")


#12.5.17

def add_py(name):
    print("%s.py" % name)
    print(name + ".py")


#12.6.17

# def add(num1, num2, num3):
#     print(num3 + num2 + num1)
#
#
# add(90, 900, 9000)

#12.7.17


def repeat(string):
    print(string)
    print(string)
    print(string)


    for x in range(3):
        print(string)

repeat("hi")


