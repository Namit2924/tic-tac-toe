from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
current_player = "X"
winner = None

winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def check_winner():
    global winner
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            winner = board[a]
            return
    if "" not in board:
        winner = "Draw"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global current_player, winner
    data = request.json
    index = data.get("index")

    if board[index] == "" and winner is None:
        board[index] = current_player
        check_winner()
        if winner is None:
            current_player = "O" if current_player == "X" else "X"

    return jsonify({
        "board": board,
        "current_player": current_player,
        "winner": winner
    })

@app.route("/reset", methods=["POST"])
def reset():
    global board, current_player, winner
    board = [""] * 9
    current_player = "X"
    winner = None
    return jsonify({
        "board": board,
        "current_player": current_player,
        "winner": winner
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)