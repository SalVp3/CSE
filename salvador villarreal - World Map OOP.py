class Room(object):
    def __init__(self, name, north,):
        self.name = name
        self.north = north

def move(self, direction):
    global current_node
    current_node = globals()[getattr(self, direction)]


# initialize rooms
ruins = Room("Ruins", '1forest', 'stone_wall', 'sign', '1garden', None)
