class Items(object):
    def __init__(self, name, value):
        self.value = value
        self.name = name

class Weapons(Items):
    def __init__(self, name, value, attack):
        super(Weapons, self).__init__(name, value)
        self.attack = attack

class Sword(Weapons):
    def __init__(self, name, value, attack):
        super(Sword, self).__init__(name, value, attack)

class Lance(Weapons):
    def __init__(self):

class Axe(Weapons):
    def __init__(self):

class Armor(Items):
    def __init__(self, name, value, defense):
        super(Armor, self).__init__(name, value)
        self.defense = defense


class Consumable(Items):
    def __init__(self, name, value, heal):
        super(Consumable, self).__init__(name, value)
        self.heal = heal


class Special(Items):
    def __init__(self, name, value):
        super(Special, self).__init__(name, value)