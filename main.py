if __name__ == "__main__":
    from files.assets.decoration import title
    from files import game, ask_user_inputs, homescreen
    from os import system

    title.display_title("files/assets/decoration/title.txt")
    print("{:^164}".format("------------------------------------------"))
    print("{:^164}".format("                Welcome !                 "))
    print("{:^164}".format("------------------------------------------"))
    input("{:^164}".format("Press <Enter> to continue"))
    system("cls")

    usr_choice = homescreen.display_menu()
    while usr_choice == 1:  # While user decides to show rules

        system("cls")
        usr_choice = homescreen.display_menu()

    if usr_choice == 2:
        game.start_playing(
            ask_user_inputs.ask_display_policy(), ask_user_inputs.ask_map(), ask_user_inputs.ask_map_size()
        )




