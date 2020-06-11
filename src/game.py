"""
TODO: List of actions needed to play the game

- player choice for movement, player inventory, or explore room
- ability to pick up item from room
- ability to drop item in room
- loop to play the game
"""


class Game:
    def __init__(self, player, room):
        self.player = player
        self.room = room

    def __str__(self):
        return f'{self.player.name}, you are currently in the {self.player.current_room.name}.'

    def play_game(self):
        explore = True
        stars = (60 - len("*")) * "*"
        while explore:
            choice = self.player.make_choice()

            try:
                if choice == 'n':
                    self.player.move_room(self.player.current_room.n_to)
                    self.player.current_room.explore_room()
                    print(self.player.current_room)
                elif choice == 's':
                    self.player.move_room(self.player.current_room.s_to)
                    self.player.current_room.explore_room()
                    print(self.player.current_room)
                elif choice == 'w':
                    self.player.move_room(self.player.current_room.w_to)
                    self.player.current_room.explore_room()
                    print(self.player.current_room)
                elif choice == 'e':
                    self.player.move_room(self.player.current_room.e_to)
                    self.player.current_room.explore_room()
                    print(self.player.current_room)
                elif choice == 'q':
                    explore = False

                else:
                    print(
                        "Please choose one of the cardinal directions, n, s, e, or w.")
            except:
                print(stars)
                print(
                    "\nYou must follow the directions the room offers, can't just go smashing through walls!")
                print("(Although that would probably be more fun)\n")
                print(stars)
                print(f"\n{self.player.current_room}")
