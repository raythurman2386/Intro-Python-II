from item import items
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, has_lighting=False, monster=None):
        self.name = name
        self.description = description
        self.has_lighting = has_lighting
        self.monster = monster
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        output = f"\n{self.name}: {self.description}\n\n"
        if self.s_to:
            output += f'To the south is: {self.s_to.name}\n'
        if self.e_to:
            output += f'To the east is: {self.e_to.name}\n'
        if self.n_to:
            output += f'To the north is: {self.n_to.name}\n'
        if self.w_to:
            output += f'To the west is: {self.w_to.name}\n'
        return output

    def show_items(self):
        i = 1
        for item in self.items:
            print(f" [{i}]: {item}")
            i += 1

    def remove_item(self, item):
        print(f"You removed the {item.name} from {self.name}")

    def add_item(self, item):
        print(f"You added {item.name} to {self.name}")


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

    'courtyard': Room("Abandoned Courtyard", """This place looks as though we 
should not be here!, Lets get out of here! Looks like there is an exit to the east."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].w_to = room['courtyard']
room['foyer'].e_to = room['narrow']
room['courtyard'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
