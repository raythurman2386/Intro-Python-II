from setup import print_stars
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
        self.explore = True

    def __str__(self):
        return f'{self.player.name}, you are currently in the {self.player.current_room.name}.'

    def location(self):
        print(f'{self.player.current_room}')
        self.player.current_room.show_items()

    def move_player(self, choice):
        if choice == 'n':
            self.player.move_room(self.player.current_room.n_to)
        elif choice == 's':
            self.player.move_room(self.player.current_room.s_to)
        elif choice == 'e':
            self.player.move_room(self.player.current_room.e_to)
        elif choice == 'w':
            self.player.move_room(self.player.current_room.w_to)

    def perform_action(self, action, item):
        index = item - 1
        if action == 'take':
            self.player.items.append(self.player.current_room.items[index])
            self.player.current_room.items.remove(
                self.player.current_room.items[index])
            print(self.player.list_items())
        if action == 'drop':
            self.player.current_room.items.append(
                self.player.items[index])
            self.player.items.remove(self.player.items[index])
            print(self.player.list_items())

    def user_input(self):
        choice = self.player.make_choice()
        if choice == 'n' or choice == 's' or choice == 'e' or choice == 'w':
            self.move_player(choice)

        elif choice == 'i' or choice == 'inventory':
            self.player.list_items()

        elif choice.split(' ')[0] == 'take' or choice.split(' ')[0] == 'drop':
            action = choice.split(' ')[0]
            item = int(choice.split(' ')[2])
            self.perform_action(action, item)

        elif choice == 'q':
            self.explore = False

        else:
            print("Please pick a valid action :)")

    # loop to play the game
    def play_game(self):
        while self.explore:
            self.location()
            self.user_input()
