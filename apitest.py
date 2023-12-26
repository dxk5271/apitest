from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/process_dataframe', methods=['POST'])
def process_dataframe():

    try:
        data = request.json


        # Create DataFrame directly from the list of dictionaries
        df = pd.DataFrame(data)
        print(df)

        # Log the DataFrame instead of printing
      

        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        app.logger.error(f"Error processing DataFrame: {str(e)}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

