class Character(object):
    def __init__(self, name, interact, health, attack, defense, inventory, description):

        self.name = name
        self.interact = interact
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.description = description


main_person = Character('Unknown', False, 30, 7, 5, None, 'you dont know who you are or how you got here')
troll = Character('Troll', None, 28, 22, 10, 'axe', 'This troll is looking at you like your it"s next meal')
skeleton = Character('Skeley bone', None, 15, 12, 5, None,
                     'There is a walking pile of bones and seems like it wants to fight')
trader = Character('Jon', True, 30, 12, 10, 'gold','Jon seems like he want to trade')
armed_troll = Character('Armored Troll', None, 26, 25, 20, 'knife',
                    'You see a troll with tough looking armored and seems want to fight you')
skeleton2 = Character('E', None, 15, 12, 5, None,
                     'There is a walking pile of bones and seems like it wants to fight')
