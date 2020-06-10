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
        while explore:
            choice = input(
                "\nPlease input n, s, w, e to move into a new room, or press 'q' to exit: ").lower()

            try:
                if choice == 'q':
                    explore = False

                if choice == 'n':
                    self.player.current_room = self.player.current_room.n_to
                    print(self.player.current_room)
                    print(f"\n{self.player.current_room.show_items()}")
                elif choice == 's':
                    self.player.current_room = self.player.current_room.s_to
                    print(self.player.current_room)
                    print(f"\n{self.player.current_room.show_items()}")
                elif choice == 'w':
                    self.player.current_room = self.player.current_room.w_to
                    print(self.player.current_room)
                    print(f"\n{self.player.current_room.show_items()}")
                elif choice == 'e':
                    self.player.current_room = self.player.current_room.e_to
                    print(self.player.current_room)
                    print(f"\n{self.player.current_room.show_items()}")

                else:
                    print(
                        "Please choose one of the cardinal directions, n, s, e, or w.")
            except:
                print(
                    "\n\n***************************************************************************************")
                print(
                    "\nYou must follow the directions the room offers, can't just go smashing through walls!")
                print("(Although that would probably be more fun)")
                print(
                    "***************************************************************************************")
                print(f"\n{self.player.current_room}")
