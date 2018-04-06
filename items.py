class Items(object):
    def __init__(self, name, value, weight):
        self.value = value
        self.name = name
        self.weight = weight


class Weapons(Items):
    def __init__(self, name, value, weight, attack):
        super(Weapons, self).__init__(name, value, weight)
        self.attack = attack


class Sword(Weapons):
    def __init__(self, name, value, weight, attack):
        super(Sword, self).__init__(name, value, weight, attack)


class Lance(Weapons):
    def __init__(self, name, value, weight, attack):
        super(Lance, self).__init__(name, value, weight, attack)


class Axe(Weapons):
    def __init__(self, name, value, weight, attack):
        super(Axe, self).__init__(name, value, weight, attack)


class Armor(Items):
    def __init__(self, name, value, weight, defense):
        super(Armor, self).__init__(name, value, weight)
        self.defense = defense


class Consumable(Items):
    def __init__(self, name, value, weight):
        super(Consumable, self).__init__(name, value, weight)


class Food(Consumable):
    def __init__(self, name, value, weight, heal):
        super(Food, self).__init__(name, value, weight,)
        self.heal = heal


apple = Food('apple', 4, 0.2, +4)
fruit1= Food('StrangeFruit', 6, 0.2, +8)


class Potions(Consumable):
    def __init__(self, name, value, weight, effect):
        super(Potions, self).__init__(name, value, weight)
        self.effect = effect


class Special(Items):
    def __init__(self, name, value, weight, description):
        super(Special, self).__init__(name, value, weight)
        self.description = description
