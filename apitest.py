from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/test', methods=['POST'])
def test_api():
    data = request.json  # Assuming the request contains a valid JSON payload
    if 'poopjelly' in data:
        return jsonify({"message": f"Received 'poopjelly' with value: {data['poopjelly']}"})
    else:
        return jsonify({"error": "The key 'poopjelly' is missing in the JSON payload"}), 400


if __name__ == '__main__':
    app.run(debug=True)
