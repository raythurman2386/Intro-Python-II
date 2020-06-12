from item import items
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"Player: {self.name} \nCurrent Room: {self.current_room}"

    def make_choice(self):
        output = """\nPlease input n, s, w, e to move into a new room, or press 'q' to exit: 
OR input I or 'inventory' to check out your inventory!
ALSO 'take item 1' will place item 1 in your inventory for example!
"""
        return input(output).lower()

    def list_items(self):
        i = 1
        if len(self.items) == 0:
            print("\nYou have no items yet!")
        for item in self.items:
            print(f'\n[{i}]: {item}')
            i += 1

    def move_room(self, room):
        self.current_room = room
        return print(f"\nYou have entered the {self.current_room.name}")

    def get_item(self, item):
        print(f"\nYou picked up {item.name}")

    def drop_item(self, item):
        print(f"\nYou dropped {item.name}")
