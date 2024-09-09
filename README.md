# Adventure Game (Flask-based)

This project is a web-based text adventure game, inspired by Crowther's original adventure game. Players explore various rooms, collect items, and interact with their environment using text commands, all within a browser interface powered by Flask.

## Features

- **Room Exploration**: Navigate through rooms by entering text commands.
- **Inventory System**: Collect and drop items as you explore the game world.
- **Synonyms Support**: Flexibility in using various synonymous commands.
- **Queue System**: A custom queue structure for managing tasks or sequences.
- **Room and Item Management**: Uses custom Python classes to handle room connections, descriptions, and item inventories.

## Project Structure

### `Room` Class

The `Room` class manages the game's environment, such as room descriptions, item inventories, and connections to other rooms.

Methods:
- `add_inventory()`: Adds items to a room's inventory.
- `description()`: Returns the room's description.
- `add_connection()`: Connects rooms together.
- `get_connection()`: Retrieves a connected room based on a direction.

### `Item` Class

The `Item` class represents objects that can be picked up, dropped, or interacted with in the game.

Methods:
- `item_description()`: Returns the description of the item.

### `Queue` Class

Implements a simple queue data structure, used to manage tasks in the game.

Methods:
- `enqueue()`: Adds a task to the queue.
- `dequeue()`: Removes a task from the queue.
- `peek()`: Returns the task at the front of the queue without removing it.
- `size()`: Returns the current size of the queue.
- `empty()`: Checks if the queue is empty.

## How It Works

- The game reads configuration files that contain room details, item descriptions, and room connections.
- Players issue commands like `TAKE`, `DROP`, `LOOK`, or directional movements to navigate and interact with the game world.
- Flask serves the web-based interface, allowing users to interact with the game via a browser.

## Installation

### Prerequisites

- **Python 3.x**
- **Flask**: Install Flask by running:
  ```
  pip install Flask
  ```

### Steps to Set Up

1. Clone the repository:
   ```
   git clone https://github.com/Justinuiterloo/Adventure-Game.git
   ```

2. Navigate to the project directory:
   ```
   cd Adventure-Game
   ```

3. Install the required packages (Flask):
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```
   flask run
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000` to start playing.

## Gameplay Commands

- **MOVE**: Navigate through rooms using directional commands such as `NORTH`, `SOUTH`, `EAST`, `WEST`.
- **LOOK**: Display the description of the current room.
- **TAKE [item]**: Add an item to your inventory.
- **DROP [item]**: Remove an item from your inventory.
- **INVENTORY**: Show the list of items you are carrying.
- **HELP**: Display the list of available commands.
- **QUIT**: Exit the game.

## Future Enhancements

- **Expanded Map**: Add more rooms and puzzles to explore.
- **Character Development**: Implement more interaction with NPCs and richer storylines.
- **Save/Load Feature**: Allow players to save their progress and resume the game later.