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


# initialize rooms
ruins = Room("Ruins", 'forest1', 'stone_wall', 'sign', 'garden1', None,
             "There are piles of stone. There are paths to the north, south, east, and west")
forest1 = Room("Spider forest", 'pit', 'ruins', 'grave', 'statue', None,
               "You've arrived at the spider forest. You can go north, south, east, and west.")
sign = Room('Stop sign', 'lagoon', 'forest2', None, 'ruins', None,
            "You're near a broken stop sign. You can go north, south, or west")
pit = Room('Deep pit', None, 'forest1', None, 'pool', None,
           "You find a giant hole in the ground. There are paths to the south and west")
pool = Room('Pool', None, 'statue', 'pit', None, None,
            "You've came across a pool. there are paths to the east and south")
statue = Room('Grand Statue', 'pool', None, 'forest1', None, 'sword',
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
    # look for which command we typed in
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
