# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f"Welcome to {self.name}!"
        output += f"\n{self.description}"
        return output
