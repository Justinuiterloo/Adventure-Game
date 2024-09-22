import loader


class Adventure:
    def __init__(self, filename):
        """
        Initializes the game by loading the map (rooms), setting up the backpack,
        and loading synonyms for user commands.
        """
        self._current_room = loader.load_room_graph(filename)
        self._backpack = {}
        self.synonyms = loader.load_synonyms("data/Synonyms.dat")

    def check_backpack(self) -> bool:
        """
        Checks if the backpack has any items.
        Returns True if there are items, False otherwise.
        """
        return len(self._backpack) > 0

    def room_description(self) -> str:
        """
        Returns the description of the current room.
        """
        return self._current_room.description()

    def move(self, direction: str) -> bool:
        """
        Attempts to move the player in a given direction.
        Returns True if the move was successful, False otherwise.
        """
        if self._current_room.has_connection(direction):
            self._current_room.set_visited()

            # Get all connections from the current room based on the given direction
            connections = self._current_room.get_connection(direction)

            for i in range(0, len(connections), 2):
                destination_room = connections[i]
                required_item = connections[i + 1]

                # Move to the destination if no item is required or if the player has the item
                if required_item is None or required_item in self._backpack:
                    self._current_room = destination_room
                    return True

        # Move not possible
        return False

    def take(self, item: str) -> bool:
        """
        Attempts to take an item from the current room and place it in the backpack.
        Returns True if successful, False if the item is not present.
        """
        if self._current_room.check_item(item):
            self._backpack[item] = self._current_room.remove_item_room(item)
            return True
        return False

    def drop(self, item: str) -> bool:
        """
        Attempts to drop an item from the backpack into the current room.
        Returns True if successful, False if the item is not in the backpack.
        """
        if item in self._backpack:
            dropped_item = self._backpack.pop(item)
            self._current_room.add_item_room(dropped_item)
            return True
        return False

    def has_forced(self) -> bool:
        """
        Checks if the current room has a forced direction to move (e.g., "FORCED").
        Returns True if forced movement is required.
        """
        return self._current_room.has_connection("FORCED")


if __name__ == "__main__":
    from sys import argv

    # Handle command-line arguments and load the appropriate game
    if len(argv) not in [1, 2]:
        print("Usage: python3 adventure.py [game_name]")
        exit(1)

    print("Loading...")

    # Set the game name from arguments or default to "Tiny"
    game_name = argv[1] if len(argv) == 2 else "Tiny"
    filename = f"data/{game_name}Adv.dat"

    # Initialize the game
    adventure = Adventure(filename)

    # Welcome the player
    print("Welcome to Adventure.\n")

    # Print the description of the starting room
    print(adventure.room_description())

    # Main game loop
    while True:
        # Get command input from the user
        command = input("> ").upper()

        # Replace command with its synonym if one exists
        if command in adventure.synonyms:
            command = adventure.synonyms[command]

        # Handle the "TAKE" command
        if command.startswith("TAKE"):
            try: 
                item = command.split()[1]

                # Attempt to take the item
                if adventure.take(item):
                    print(f"{item} taken.")
                else:
                    print("No such item.")
            except IndexError:
                print("You must specify an item to take")

        # Handle the "DROP" command
        elif command.startswith("DROP"):
            try: 
                item = command.split()[1]

                # Attempt to drop the item
                if adventure.drop(item):
                    print(f"{item} dropped.")
                else:
                    print("No such item.")
            except IndexError:
                print("You must specify an item to drop")



        # Handle the "LOOK" command
        elif command == "LOOK":
            # Reset the room visitation status to provide a long description
            adventure._current_room.set_devisited()
            print(adventure.room_description())
            adventure._current_room.print_inventory()
            adventure._current_room.set_visited()

        # Handle the "INVENTORY" command
        elif command == "INVENTORY":
            if not adventure.check_backpack():
                print("Your inventory is empty.")
            else:
                for key, value in adventure._backpack.items():
                    print(value.item_description())

        # Handle the "HELP" command
        elif command == "HELP":
            print("You can move by typing directions such as EAST/WEST/IN/OUT.")
            print("QUIT quits the game.")
            print("HELP prints instructions for the game.")
            print("LOOK lists the complete description of the room and its contents.")
            print("INVENTORY lists all items in your inventory.")

        # Handle movement commands (directions)
        elif not adventure.move(command):
            print("Invalid command")
        
                # Handle the "QUIT" command to exit the game
        elif command == "QUIT":
            break

        # Describe the new room and its inventory after a successful move
        else:
            print(adventure.room_description())
            adventure._current_room.print_inventory()

        # Automatically handle forced movements
        while adventure.has_forced():
            adventure.move("FORCED")
            print(adventure.room_description())
