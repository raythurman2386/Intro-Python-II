from setup import initialize_player, randomize_items
from room import room
from game import Game

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def main():
    print("\nWelcome traveler!")
    player = initialize_player()
    randomize_items()
    Game(player, room).play_game()


if __name__ == '__main__':
    main()
