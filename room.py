import string

from item import Item


class Room:

    def __init__(self, id, name, description):
        """
        removes an item from room inventory
        """
        self.id = id
        self.name = name
        self._description = description
        self._flag = False
        self.connections = {}
        self.inventory = {}


    def add_inventory(self, name: string, item: Item):
        """
        Add item to room inventory.
        """
        self.inventory[name] = item

    def set_visited(self):
        """
        Returns flag to true when player already visited in a room.
        """
        self._flag = True

    def set_devisited(self):
        """
        Returns flag to false even when player already visted the room
        """
        self._flag = False

    def description(self):
        """
        returns a certain description based on the flag of the room
        """
        if self._flag == False:
            return self._description
        elif self._flag == True:
            return self.name

    def add_connection(self, direction, room, item):
        """
        add connection to certain rooms and also adds items
        """
        if direction in self.connections:
            self.connections[direction].extend([room, item])
        else:
            self.connections[direction] = [room, item]

    def has_connection(self, direction):
        """
        Will return True is Room has a connecion with another room given a direction
        """
        if direction in self.connections:
            return True
        return False

    def get_connection(self, direction):
        """
        returns the room that has a connection given a direction
        """
        return self.connections[direction]

    def print_inventory(self):
        """
        prints items and there description in a room
        """
        for key, value in self.inventory.items():
            print(value.item_description())

    def check_item(self, item):
        """
        returns the room that has a connection given a direction
        """
        if item in self.inventory:
            return True
        return False

    def remove_item_room(self, item):
        """
        removes an item from room inventory
        """
        keys = self.inventory[item]
        del self.inventory[item]
        return keys

    def add_item_room(self, item):
        """
        add item to inventory of room
        """
        self.inventory[item._item_name] = item
