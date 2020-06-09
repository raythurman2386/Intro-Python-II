# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"Player: {self.name} \nCurrent Room: {self.current_room}"

    def get_item(self, item):
        return self.items.append(item)
