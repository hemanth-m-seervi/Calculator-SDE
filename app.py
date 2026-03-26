from flask import Flask, request, jsonify
from flask_cors import CORS  # allows frontend to call API

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

@app.route("/calc", methods=["GET"])
def calculate():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        op = request.args.get("op")

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            if b == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = a / b
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)