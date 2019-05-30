import sys
from room import Room
from player import Player
from item import Item
from item import LightSource
from dragon import Dragon

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True, False),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True, False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False, False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", True, True),
    'cavern': Room("Dark Cavern", """It sounds like you have stepped into a
damp cavern... it's really dark in here but the echo makes
it seem like it is a really big room""", False, False),
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
room['narrow'].e_to = room['cavern']
room['cavern'].w_to = room['narrow']

# items in rooms
room['foyer'].add_item(Item('chest', 'Wonder what is in here?'))
room['outside'].add_item(Item('dagger', 'small dagger... it is kinda dull'))
room['outside'].add_item(Item('necklace', 'A dirty necklace... try wiping it off'))
room['overlook'].add_item(Item('key', 'tiny bronze key'))
room['treasure'].add_item(Item('bottle', 'Seems to contain a message'))
room['cavern'].add_item(LightSource('torch', 'Bet this will help in dark areas...'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

ruby = Player('Ruby', room['outside'])
drake = Dragon("Fire Drake",100, 100, room['treasure'])


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

directions = ('n', 'e', 's', 'w')

while True:
    print(f"Room: {ruby.current_room.name}\n")
    if ruby.current_room.is_light or [item.name == 'torch' for item in
                                              ruby.items]:
      print(ruby.current_room.description)
      print("Items around room: \n", end='')
      print([item.name for item in ruby.current_room.items])
      if ruby.current_room.has_boss:
          print(f"{drake.name}: {drake.health}, {drake.source_mana}")
    else:
      print("It's pitch black \n")
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

    elif cmd == 'i':
        print("Inventory: ", end="")
        print([item.name for item in ruby.items])

    else:
        cmds = cmd.split(' ')

        if len(cmds) != 2:
            print('Bad Command!')
        else:
            verb, obj = cmds
            if verb == 'take':
                try:
                    item = [x for x in ruby.current_room.items if x.name == obj][0]
                    ruby.current_room.remove_item(item)
                    ruby.add_item(item)
                    item.on_take()
                except IndexError:
                    print('Item not found!')
            elif verb == 'drop':
                try:
                    item = [x for x in ruby.items if x.name == obj][0]
                    if item.on_drop():
                        ruby.current_room.add_item(item)
                        ruby.remove_item(item)
                except IndexError:
                    print('player not holding item')
            else:
                print("Bad Command!")


