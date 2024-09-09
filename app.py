from flask import Flask, jsonify, request, render_template
from adventure import Adventure

app = Flask(__name__, static_folder='static')

game = Adventure("data/TinyAdv.dat")

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/start", methods=["GET"])
def start_game():
    return jsonify(description=game.room_description())

@app.route("/command", methods=["POST"])
def handle_command():
    command = request.json.get("command").upper()
    response = ""

    # Command handling logic
    if command == "LOOK":
        response = game.room_description()
    elif command.startswith("TAKE"):
        item = command.split()[1]
        if game.take(item):
            response = f"{item} taken"
        else:
            response = "No such item."
    elif command.startswith("DROP"):
        item = command.split()[1]
        if game.drop(item):
            response = f"{item} dropped"
        else:
            response = "No such item."
    elif game.move(command):
        response = game.room_description()
    else:
        response = "Invalid command."

    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)
