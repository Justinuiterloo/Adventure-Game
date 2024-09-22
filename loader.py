from room import Room
from item import Item


def load_room_graph(filename: str) -> Room:
    """
    Loads rooms, their connections, and items from a structured text file.
    
    The file should contain three sections:
    1. Room information (id, name, description)
    2. Room connections (source room, direction, destination room, optional item)
    3. Item information (item name, description, room id)
    
    Parameters:
        filename (str): The file path containing room, connection, and item information.

    Returns:
        Room: The starting room (usually the room with id 1).
    """
    rooms = {}  # Dictionary to store rooms by their id

    # Read and process the file
    with open(filename) as f:
        # Step 1: Load room information
        _load_rooms(f, rooms)
        
        # Step 2: Load room connections
        _load_connections(f, rooms)
        
        # Step 3: Load items and assign them to the appropriate rooms
        _load_items(f, rooms)

    # Return the initial room, typically with id 1
    return rooms[1]


def _load_rooms(f, rooms: dict):
    """
    Internal function to load room data from the file.
    Reads lines until a blank line is found.
    """
    while True:
        line = f.readline().strip()

        # Break at an empty line, indicating the end of room information
        if not line:
            break

        # Split each line by tab to extract room details (id, name, description)
        room_id, name, description = line.split("\t")

        # Create a Room object and store it in the rooms dictionary
        rooms[int(room_id)] = Room(int(room_id), name, description)


def _load_connections(f, rooms: dict):
    """
    Internal function to load room connections from the file.
    Reads lines until a blank line is found.
    """
    while True:
        line = f.readline().strip()

        # Break at an empty line, indicating the end of connection information
        if not line:
            break

        # Extract the source room and its connections
        connection_data = line.split("\t")
        source_room_id = int(connection_data[0])
        source_room = rooms[source_room_id]

        # Iterate over connections, parsing each direction and destination
        for i in range(1, len(connection_data), 2):
            direction = connection_data[i]
            destination_info = connection_data[i + 1]

            if "/" in destination_info:
                # If an item is needed for the connection
                destination_room_id, required_item = destination_info.split("/")
                destination_room = rooms[int(destination_room_id)]
                source_room.add_connection(direction, destination_room, required_item)
            else:
                # Simple connection without an item
                destination_room = rooms[int(destination_info)]
                source_room.add_connection(direction, destination_room, None)


def _load_items(f, rooms: dict):
    """
    Internal function to load item data from the file.
    Reads lines until the end of the file.
    """
    while True:
        line = f.readline().strip()

        # Break at the end of the file
        if not line:
            break

        # Split the line by tab to extract item details
        item_name, item_description, room_id = line.split("\t")

        # Create an Item object and add it to the specified room
        item = Item(item_name, item_description)
        rooms[int(room_id)].add_inventory(item_name, item)


def load_synonyms(filename: str) -> dict:
    """
    Loads synonyms for command input from a structured text file.
    
    The file should contain lines with the format `command=synonym`.
    
    Parameters:
        filename (str): The file path containing synonym data.

    Returns:
        dict: A dictionary mapping commands to their synonyms.
    """
    synonyms = {}  # Dictionary to store command synonyms

    # Read and process the synonym file
    with open(filename) as f:
        while True:
            line = f.readline().strip()

            # Stop at the end of the file
            if not line:
                break

            # Split each line by '=' to extract command and synonym
            command, synonym = line.split("=")
            synonyms[command] = synonym

    return synonyms
