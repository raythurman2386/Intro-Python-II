from random import choice
from room import room
from item import items
from player import Player


# Make a new player object that is currently in the 'outside' room.
def initialize_player():
    player_name = input("Please tell us your name :) ").capitalize()
    print(f"\nWell, {player_name} prepare for a whirlwind of an adventure!")
    print(f"{room['outside']}")
    return Player(player_name, room['outside'])


# TODO: Need to randomly generate items to random rooms
def randomize_items():
    for item in range(len(items)):
        random_room = choice([i for i in room])
        random_item = choice([i for i in items])
        del items[random_item]
        room[random_room].items.append(random_item)
