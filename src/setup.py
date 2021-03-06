from random import choice
from textwrap import wrap, indent
from room import room
from item import items
from player import Player


# Make a new player object that is currently in the 'outside' room.
def initialize_player():
    player_name = input("Please tell us your name :) ").capitalize()
    print(f"\nWell, {player_name} prepare for a whirlwind of an adventure!")
    return Player(player_name, room['outside'])


# TODO: Need to randomly generate items to random rooms
def randomize_items():
    for item in range(len(items)):
        random_room = choice([i for i in room])
        random_item = choice([i for i in items])
        room[random_room].items.append(random_item)


def print_stars():
    print((60 - len("*")) * "*")


def format_print(str):
    print(wrap(indent(str, '>    '), width=60))
