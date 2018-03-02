world_map = {
    'RUINS': {
        'NAME': "Ruins",
        'DESCRIPTION': "There are piles of stone. There are paths to the north, south, east, and west",
        'PATHS': {
            'NORTH': '1FOREST',
            'SOUTH': 'STONEWALL',
            'EAST': 'SIGN',
            'WEST': '1GARDEN'
        }
    },
    '1FOREST': {
        'NAME': 'Spider forest',
        'DESCRIPTION': " You've arrived at the spider forest. You can go north, south, east, and west",
        'PATHS': {
            'NORTH': 'PIT',
            'EAST': 'GRAVE',
            'WEST': 'STATUE',
            'SOUTH': 'RUINS'
        }
    },
    'SIGN': {
        'NAME': "Stop sign",
        'DESCRIPTION': "You're near a broken stop sign. You can go north, south, or west",
        'PATHS': {
            'NORTH': 'LAGOON',
            'SOUTH': '2FOREST',
            'WEST': 'RUINS'
        }
    },
    'PIT': {
        'NAME': "Deep Pit",
        'DESCRIPTION': "You find a giant hole in the ground. There are paths to the south and west",
        'PATHS': {
            'SOUTH': '1FOREST',
            'WEST': 'POOL'
        }
    },
    'POOL': {
        'NAME': "Pool",
        'DESCRIPTION': "You've came across a pool. there are paths to the east and south",
        'PATHS': {
            'EAST': 'PIT',
            'SOUTH': 'STATUE'
        }
    },
    'STATUE': {
        'NAME': "Grand Statue",
        'DESCRIPTION': "You arrive at the grand statue and it holding a sword. You can go north or east",
        'PATHS': {
            'NORTH': 'POOL',
            'EAST': '1FOREST'
        }
    },
    'GRAVE': {
        'NAME': "Grave Yard",
        'DESCRIPTION': "you enter a misty grave yard, you see a shield. You can only go west.",
        'PATHS': {
            'WEST': '1FOREST'
        }
    },
    'LAGOON': {
        'NAME': "Black lagoon",
        'DESCRIPTION': "You",
        'PATHS': {
        }
    },
    '': {
        'NAME': "",
        'DESCRIPTION': "",
        'PATHS': {
        }
    },
}

current_node = world_map['RUINS']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("you cannot go this way")
    else:
        print('Command not Recognized')
    print()
