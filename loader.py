def load_room_graph(filename):
    """
    load rooms, directions and items.
    """
    from room import Room
    from item import Item

    # Two dicitonairies with items and rooms
    items = {}
    rooms = {}

    # Read the first part of the text file with room info
    with open(filename) as f:
        while True:

            # Read every line until an enter is found
            line = f.readline()
            if line == "\n":
                break

            # Put every information of a room and store it as an object
            # Put this information in a dicitonairy
            room_info = line.strip().split("\t")
            id = room_info[0]
            name = room_info[1]
            description = room_info[2]
            rooms[id] = Room(id, name, description)

        # Now read the second part of the information until the second enter
        line = f.readline()
        while line != "\n":

            # Put every information about the room connections in some variables
            connections = line.rstrip().split("\t")
            id = connections[0]
            source_room = rooms[id]

            # Add connections based on the vairables
            for i in range(1,len(connections),2):

                #add connections without items
                if "/" in connections[i+1]:
                    direction = connections[i]
                    destination_room, item = connections[i+1].split("/")
                    source_room.add_connection(direction, rooms[destination_room], item)

                # Add connections with items
                else:
                    direction = connections[i]
                    destination_room = rooms[connections[i+1]]
                    item = None
                    source_room.add_connection(direction, destination_room, item)
            line = f.readline()

        # Read the third part of the file until the ends
        line = f.readline()
        while line != "":

            # Add every item to an room object in a dictionairy called inventory
            item = line.strip().split("\t")
            name = item[0]
            description = item[1]
            room = item[2]
            item = Item(name, description)
            rooms[room].add_inventory(name, item)
            line = f.readline()

        return rooms['1']
def loader_synonyms(filename):
    """
    Load synonyms for command input.
    """

    # Make a dictionairy with synonyms
    synonyms = {}

    # Read the third part of file textfile
    with open(filename) as f:
        line = f.readline()

        # Stop at the end of the file
        while line != "":

            # Put every synonym of a word in a dictionry
            # Return the whole dictionairy
            synonym_info = line.strip().split("=")
            letter = synonym_info[0]
            word = synonym_info[1]
            synonyms[letter] = synonym_info[1]
            line = f.readline()
    return synonyms
