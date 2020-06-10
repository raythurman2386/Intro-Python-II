import random
from room import Room
from player import Player
from game import game
from item import items

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


# Make a new player object that is currently in the 'outside' room.
def initialize_player():
    player_name = input("Please tell us your name :) ").capitalize()
    return Player(player_name, room['outside'])


# TODO: Need to randomly generate items to random rooms
def randomize_items(items, room):
    for item in range(len(items)):
        random_room = random.choice([i for i in room])
        random_item = random.choice([i for i in items])
        del items[random_item]
        room[random_room].items.append(random_item)

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


def main():
    print("\nWelcome traveler!")
    player = initialize_player()
    randomize_items(items, room)
    print(f"\nWell, {player.name} prepare for a whirlwind of an adventure!")
    print(f"\n{player.current_room}")
    explore = True
    game(explore, player)


if __name__ == '__main__':
    main()
