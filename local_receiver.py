# local_receiver.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive():
    data = request.get_json(silent=True)
    print("Received payload (local):", data and list(data.keys()))
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
