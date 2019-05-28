import sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# items in rooms
room['foyer'].add_item(Item('chest', 'Wonder what is in here?'))
room['outside'].add_item(Item('dagger', 'small dagger... it is kinda dull'))
room['outside'].add_item(Item('necklace', 'A dirty necklace... try wiping it off'))
room['overlook'].add_item(Item('key', 'tiny bronze key'))
room['treasure'].add_item(Item('bottle', 'Seems to contain a message'))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

ruby = Player('Ruby', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 'e', 's', 'w']

while True:
    print(f"Room: {ruby.current_room.name}")
    print(ruby.current_room.description)
    print("Items around room: ", end='')
    print([item.name for item in ruby.current_room.items])
    cmd = str(input('q to quit...(blue pill), continue with direction (red pill)'))

    if cmd == '' or cmd != str:
        print("Must enter 'n','s','e','w'... or 'q' to quit the game")
    if cmd == 'q':
        sys.exit()

    elif cmd in directions:
        try:
            ruby.current_room = getattr(ruby.current_room, f'{cmd}_to')
        except:
            print('apparently those who wander are lost... you can not go that way.')


