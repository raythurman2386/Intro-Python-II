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
        return input(
            "Please input n, s, w, e to move into a new room, or press 'q' to exit: ").lower()

    def move_room(self, room):
        self.current_room = room
        return print(f"\nYou have entered the {self.current_room.name}")

    def get_item(self, item):
        self.current_room.remove_item(item)
        self.items.append(item)
        return f"You picked up {item.name}"

    def drop_item(self, item):
        self.current_room.add_item(item)
        del self.items[item]
        return f"You dropped {item.name}"
