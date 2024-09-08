# adventure.py
#
# Justin D. Uiterloo
#
# - plays Crowthers game

import loader

class Adventure():


    def __init__(self, filename):
        """
         Loads map with rooms, initialize backpack and loads synonyms
        """
        self._current_room = loader.load_room_graph(filename)
        self._backpack = {}
        self.synonyms = loader.loader_synonyms("data/Synonyms.dat")

    def check_backpack(self):
        """
        returns the room that has a connection given a direction
        """
        if len(self._backpack) == 0:
            return False
        return True


    def room_description(self):
        """
         Returns description of room.
        """
        return self._current_room.description()


    def move(self, direction):
        """
        Checks if move is possible and if it is. Do a move in a certain direction!
        """
        if self._current_room.has_connection(direction):
            self._current_room.set_visited()

            # Get the connections of current room to next room, based on given direction
            current_connections = self._current_room.get_connection(direction)

            for i in range(0, len(current_connections), 2):

                if current_connections[i + 1] is None:
                    self._current_room = current_connections[i]
                    # Move was possible,return true
                    return True
                else:
                    # Check if user has item, if so, go to room
                    if current_connections[i+1] in self._backpack:
                        self._current_room = current_connections[i]
                        return True
        # If move was not possible, return false
        return False

    def take(self, item):
        """
        Checks if an item is in a room. If item is there. Put item in backpack.
        """
        if self._current_room.check_item(item):
            self._backpack[item] = self._current_room.remove_item_room(item)
            return True
        return False

    def drop(self, item):
        """
        Checks if an item is in a backpack. If item is there. Put item in room.
        """
        if item in self._backpack:
            keys = self._backpack[item]
            del self._backpack[item]
            self._current_room.add_item_room(keys)
            return True
        return False


    def has_forced(self):
        """
        Checks if room has a direction "FORCED".
        """
        if self._current_room.has_connection("FORCED"):
            return True
        return False



if __name__ == "__main__":

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1,2]:
        print("Usage: python3 adventure.py [name]")
        exit(1)

    # Load the requested game or else Tiny
    print("Loading...")
    if len(argv) == 2:
        game_name = argv[1]
    elif len(argv) == 1:
        game_name = "Tiny"
    filename = f"data/{game_name}Adv.dat"

    # Create game
    adventure = Adventure(filename)

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.room_description())

    # Prompt the user for commands until they type QUIT
    while True:

        # Get command from user
        command = input("> ").upper()

        # Checks if input is synonym and uses the right move
        if command in adventure.synonyms:
            command = adventure.synonyms[command]

        # Checks if "TAKE" is in command and uses take() fuction
        if "TAKE" in command:
            command = command.split()

            # Checks second string in iput is the item in the room
            # If item in de room, the take function wil be excecuted
            # Else the user will be told that there is no item in the room
            if adventure.take(command[1]):
                print(f"{command[1]} taken")
            else:
                print("No such item.")

        # Checks if  "DROP" is in command and uses drop() fuction
        elif "DROP" in command:
            command = command.split()

            # Checks second string in iput is the item in the room
            # If item in de backpack, the drop function wil be excecuted
            # Else the user will be told that there is no item in backpack
            if adventure.drop(command[1]):
                print(f"{command[1]} dropped")
            else:
                print("No such item.")

        # Checks if  "LOOK" is in command
        # If the command is "LOOK", the long room description is printed
        # Also the items in the room wil be printed
        elif "LOOK" in command:
            adventure._current_room.set_devisited()
            print(adventure.room_description())
            adventure._current_room.print_inventory()
            adventure._current_room.set_visited()

        # Checks if  "INVENTORY" is in command
        # If the command is "INVENTORY", the items in backpack will be printed
        elif "INVENTORY" in command:
            if adventure.check_backpack() is False:
                print("Your inventory is empty")
            else:
                for keys,value in adventure._backpack.items():
                    print(value.item_desciption())

        # Checks if  "HELP" is in command
        # If the command is "HELP", alle possible commands will printed
        # except for the directions
        elif "HELP" in command:
            print("You can move by typing directions such as EAST/WEST/IN/OUT")
            print("QUIT quits the game.")
            print("HELP prints instructions for the game.")
            print("LOOK lists the complete description of the room and its contents.")
            print("INVENTORY lists all items in your inventory.")


        # Checks if the move() fuctions returns False
        # If the move() function returns falls
        # "Invalid command" will be printed
        elif adventure.move(command) == False:
            print("Invalid command")

        # If the move() function returns True
        # The room description and inventory of that room will be printed
        else:
            print(adventure.room_description())
            adventure._current_room.print_inventory()

        # This Loop will always check if the move() function
        # Can do a forced movement and print the room description
        while adventure.has_forced() == True:
            adventure.move("FORCED")
            print(adventure.room_description())





        # Allows player to exit the game loop
        if command == "QUIT":
            break
