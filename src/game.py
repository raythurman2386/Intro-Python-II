from setup import print_stars
"""
TODO: List of actions for lighting

- Check for has_lighting on room entrance
    - if no light, equip Torch
        - if no Torch return to previous room
- otherwise continue on
"""

"""
TODO: List of actions needed for monsters

- Randomly add monsters to room
- ability to choose fight or run
- player can only fight if has weapon
- fight starts loop for attacking
    - player attacks
    - monster attacks
    - till player or monster health == 0
        - if player dies, game over
        - if monster dies game continues on
- run sends player to previous room
"""


class Game:
    def __init__(self, player, room):
        self.player = player
        self.room = room
        self.explore = True

    def __str__(self):
        return f'{self.player.name}, you are currently in the {self.player.current_room.name}.'

    # Print the location on each iteration of the loop
    def location(self):
        print(f'{self.player.current_room}')
        self.player.current_room.show_items()

    # Move the player in a given direction
    def move_player(self, choice):
        if choice == 'n':
            if self.player.current_room.n_to == None:
                print("You cannot go that way goober!")
                self.user_input()
            self.player.move_room(self.player.current_room.n_to)
        elif choice == 's':
            if self.player.current_room.s_to == None:
                print("You cannot go that way goober!")
                self.user_input()
            self.player.move_room(self.player.current_room.s_to)
        elif choice == 'e':
            if self.player.current_room.e_to == None:
                print("You cannot go that way goober!")
                self.user_input()
            self.player.move_room(self.player.current_room.e_to)
        elif choice == 'w':
            if self.player.current_room.w_to == None:
                print("You cannot go that way goober!")
                self.user_input()
            self.player.move_room(self.player.current_room.w_to)

    # Perform an action with an item
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

    # Get user input
    # Decide what to do with said input
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
            print("Hope you had a good time! Come back soon!")
            self.explore = False
        else:
            print("Please pick a valid action :)")

    # loop to play the game
    def play_game(self):
        while self.explore:
            try:
                self.location()
                self.user_input()
            except:
                print("There has been an error, I am sorry :( ")
