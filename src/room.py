# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f"\nWelcome to the {self.name}!"
        output += f"\n\n{self.description}"
        return output
