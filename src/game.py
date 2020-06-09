def game(explore, player):
    while explore:
        choice = input(
            "\nPlease input n, s, w, e to move into a new room, or press 'q' to exit: ").lower()

        try:
            if choice == 'q':
                explore = False

            if choice == 'n':
                player.current_room = player.current_room.n_to
                print(player.current_room)
            elif choice == 's':
                player.current_room = player.current_room.s_to
                print(player.current_room)
            elif choice == 'w':
                player.current_room = player.current_room.w_to
                print(player.current_room)
            elif choice == 'e':
                player.current_room = player.current_room.e_to
                print(player.current_room)

            else:
                print("Please choose one of the cardinal directions, n, s, e, or w.")
        except:
            print(
                "\n\n***************************************************************************************")
            print(
                "\nYou must follow the directions the room offers, can't just go smashing through walls!")
            print("(Although that would probably be more fun)")
            print(
                "***************************************************************************************")
            print(f"\n{player.current_room}")
