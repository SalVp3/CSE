class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job, income):
        super(Employee, self).__init__(name, age)
        self.job = job
        self.income = income

    def info(self):
        print("%s works as a " % self.name + self.job, ". He earns $%s a day" % self.income)


class Programmer(Employee):
    def __init__(self, intelligence):
        super(Programmer, self).__init__()
        self.int = intelligence

    def info2(self):
        print("%s has an a intelligence of" % self.name + self.int)


person1 = Employee('John', 25, 'Programmer', 1000)
person1.work()
person1.info()
person2 = Employee('Mike', 30, 'programmer', 200)
person2.info()