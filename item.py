class Item:
    def __init__(self, name, description):
        """
        initialize an object: item based on name and discription
        """
        self._item_name = name
        self._item_description = description


    def item_description(self):
        """
        Return the descriptions of items based on the namen en descption attributes
        """
        return f"{self._item_name} :{self._item_description}"
