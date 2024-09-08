# Adventure Game

This project is a text-based adventure game inspired by Crowther's original. Players explore rooms, collect items, and interact with their surroundings using text commands.

## Features

* **Room Exploration**: Move between rooms by entering commands.
* **Inventory System**: Collect and drop items as you explore.
* **Synonyms Support**: Players can use synonymous commands for flexibility.
* **Queue System**: A custom queue implementation for managing tasks or sequences.
* **Room and Item Management**: The game uses custom classes to manage room connections and inventory items.

## Classes

### Room
Manages room descriptions, connections, and inventory.
* `add_inventory()`, `description()`, `add_connection()`, `get_connection()`.

### Item
Represents objects that can be picked up or dropped.
* `item_description()` returns the description of an item.

### Queue
A simple queue data structure.
* `enqueue()`, `dequeue()`, `peek()`, `size()`, and `empty()` methods.

## How It Works

* The game reads from a file containing room data, item descriptions, and room connections.
* Players navigate between rooms, collect items, and issue commands like `TAKE`, `DROP`, and `LOOK`.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Justinuiterloo/Aventure-Game.git
```

2. Run the game:

```bash
python3 adventure.py
```

## Commands

* **MOVE**: Type directions like `EAST`, `WEST`, `IN`, `OUT` to move between rooms.
* **LOOK**: Displays the description of the current room.
* **TAKE [item]**: Add an item to your inventory.
* **DROP [item]**: Remove an item from your inventory.
* **INVENTORY**: Show the items in your backpack.
* **HELP**: Display help instructions.
* **QUIT**: Exit the game.
