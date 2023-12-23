from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/process_dataframe', methods=['POST'])
def process_dataframe():
    try:
        # Assuming the request contains a valid JSON payload with the DataFrame
        data = request.json

        # Explicitly provide an index when constructing the DataFrame
        df = pd.DataFrame([data], index=[0])

        # Print the DataFrame
        print("Received DataFrame:")
        print(df)

        # Return the DataFrame as JSON
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
