class Character(object):
    def __init__(self, name, interact, health, attack, defense, inventory, description):

        self.name = name
        self.interact = interact
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.description = description

    def interaction(self):
        self.interact = False
        self.talk = True


troll = Character('Troll', None, 28, 22, 10, 'axe', 'This troll is looking at you like your it"s next meal')
skeleton = Character('Skeley bone', None, 15, 12, 5, None,
                     'There is a walking pile of bones and seems like it wants to fight')
trader = Character('Jon', True, 30, 12, 10, 'gold', 'Jon seems like he want to trade')
