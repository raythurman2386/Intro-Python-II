class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item: {self.name}\nDesc: {self.description}"


items = {
    "Gold Coin": Item("Gold Coin", "Gold coin, looks like it could be of some value."),
    "Health Potion": Item("Health Potion", "Hmmmmm, what could I possibly need this for??"),
    "Mana Potion": Item("Mana Potion", "Says on the bottle restores mana.... WTF is mana?"),
    "Thunderfury": Item("Thunderfury", "Did you say: THUNDERFURY, BLESSED BLADE OF THE WINDSEEKER!"),
    "Rusty Spoon": Item("Rusty Spoon", "Rusty spoon, looks like there is still some food on it."),
    "Pudding Cup": Item("Pudding Cup", "Who doesn't have time for pudding??"),
    "Nerf Gun": Item("Nerf Gun", "You may want this to protect yourself!"),
    "Funko Pop": Item("Funko Pop", "Kinda looks like Goku"),
    "Water Fountain": Item("Water Fountain", "This could be handy, lets just put this in the back pocket."),
    "Random Spaghetti": Item("Random Spaghetti", "No sauce.....Just noodles"),
}
