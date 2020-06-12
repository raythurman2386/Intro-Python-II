class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item: {self.name}\nDesc: {self.description}"


class Weapon(Item):
    def __init__(self, name, description, damage, quality):
        super().__init__(name, description)
        self.damage = damage
        self.quality = quality


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value


items = {
    "Gold Coin": Treasure("Gold Coin", "Gold coin, looks like it could be of some value.", "5 dolla"),
    "Health Potion": Item("Health Potion", "Hmmmmm, what could I possibly need this for??"),
    "Mana Potion": Item("Mana Potion", "Says on the bottle restores mana.... WTF is mana?"),
    "Thunderfury": Weapon("Thunderfury", "Did you say: THUNDERFURY, BLESSED BLADE OF THE WINDSEEKER!", "over9000", "Legendary"),
    "Rusty Spoon": Item("Rusty Spoon", "Rusty spoon, looks like there is still some food on it."),
    "Pudding Cup": Item("Pudding Cup", "Who doesn't have time for pudding??"),
    "Nerf Gun": Weapon("Nerf Gun", "You may want this to protect yourself!", "Negative 4", "Plastic"),
    "Funko Pop": Item("Funko Pop", "Kinda looks like Goku"),
    "Water Fountain": Item("Water Fountain", "This could be handy, lets just put this in the back pocket."),
    "Random Spaghetti": Weapon("Random Spaghetti", "No sauce.....Just noodles", "One slimy point", "OODLES OF NOODLES"),
}
