class Monster:
    def __init__(self, type, health, damage):
        self.type = type
        self.health = health
        self.damage = damage

    def __str__(self):
        print(f"The monster has {str(self.health)} left!")

    def take_damage(self, damage):
        self.health -= damage
        print(
            f"The monster takes {str(damage)} damage and has {str(self.health)} health left.")

    def deal_damage(self):
        pass


monsters = {
    "blue_monster": Monster("Troll", 24, 4),
    "red_monster": Monster("Orc", 18, 3),
    "green_monster": Monster("Ogre", 26, 2),
    "yellow_monster": Monster("Chuck Norris", 100, 1000)
}
