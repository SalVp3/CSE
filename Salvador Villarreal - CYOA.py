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


rusty_sword = Sword('Rusty sword', 1, 3, 9)
flaming_sword = Sword('Flaming sword', 10, 4.5, 28)
gold_sword = Sword('Gold sword', 12, 6.2, 20)

class Lance(Weapons):
    def __init__(self, name, value, weight, attack, defense):
        super(Lance, self).__init__(name, value, weight, attack)
        self.defense = defense


ice_lance = Lance('Ice lance', 9, 4.9, 25, 0)
broken_lance = Lance('Broken lance', 2, 2, 8, 0)
shield_lance = Lance('Shield lance', 11, 5, 12, 15)


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


class Character(object):
    def __init__(self, name, interact, health, attack, defense, inventory, description):

        self.name = name
        self.interact = interact
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.description = description


class Room(object):
    def __init__(self, name, north, south, east, west, item, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.item = item
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


troll = Character('Troll', None, 28, 22, 10, 'axe', 'This troll is looking at you like your it"s next meal')
skeleton = Character('Skeley bone', None, 15, 12, 5, None,
                     'There is a walking pile of bones and seems like it wants to fight')
trader = Character('Jon', True, 30, 12, 10, 'gold','Jon seems like he want to trade')
armed_troll = Character('Armored Troll', None, 26, 25, 20, 'knife',
                    'You see a troll with tough looking armored and seems want to fight you')
skeleton2 = Character('E', None, 15, 12, 5, None,
                     'There is a walking pile of bones and seems like it wants to fight')

# initialize rooms
ruins = Room("Ruins", 'forest1', 'stone_wall', 'sign', 'garden1', 'sword',
             "There are piles of stone. There are paths to the north, south, east, and west")
forest1 = Room("Spider forest", 'pit', 'ruins', 'grave', 'statue', None,
               "You've arrived at the spider forest. You can go north, south, east, and west.")
sign = Room('Stop sign', 'lagoon', 'forest2', None, 'ruins', None,
            "You're near a broken stop sign. You can go north, south, or west")
pit = Room('Deep pit', None, 'forest1', None, 'pool', None,
           "You find a giant hole in the ground. There are paths to the south and west")
pool = Room('Pool', None, 'statue', 'pit', None, None,
            "You've came across a pool. there are paths to the east and south")
statue = Room('Grand Statue', 'pool', None, 'forest1', None, 'golden sword',
              "You arrive at the grand statue and it holding a sword. You can go north or east")
grave = Room('Grave Yard', None, None, None, 'forest1', 'shield',
             "you enter a misty grave yard, you see a shield. You can only go west.")

current_node = ruins
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_direction:

        pos = short_direction.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("you cannot go this way")
    else:
        print('Command not Recognized')
    print()
