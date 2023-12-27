from flask import Flask, request, jsonify

app = Flask(__name__)

file_name_data = {"file_name": None, "json_data": None}

@app.route('/api/upload_file_name', methods=['POST'])
def upload_file_name():
    try:
        data = request.get_json()
        file_name_data["file_name"] = data.get("file_name")

        if file_name_data["json_data"] is not None:
            # If both file name and JSON data are available, process them
            process_data()
            return jsonify({"message": "Processing data"}), 200
        else:
            return jsonify({"message": "File name received"}), 200

    except Exception as e:
        app.logger.error(f"Error uploading file name: {str(e)}")
        return jsonify({"error": str(e)}), 400

@app.route('/api/process_dataframe', methods=['POST'])
def upload_json_data():
    try:
        data = request.get_json()
        file_name_data["json_data"] = data

        if file_name_data["file_name"] is not None:
            # If both file name and JSON data are available, process them
            process_data()
            return jsonify({"message": "Processing data"}), 200
        else:
            return jsonify({"message": "JSON data received"}), 200

    except Exception as e:
        app.logger.error(f"Error uploading JSON data: {str(e)}")
        return jsonify({"error": str(e)}), 400

def process_data():
    # Access the global dictionary to get the file name and JSON data
    file_name = file_name_data["file_name"]
    json_data = file_name_data["json_data"]

    # Your existing logic to create a DataFrame and print it
    df = pd.DataFrame(json_data)
    print("Niceee man! File Name:", file_name)
    print(df)

    # Reset the global dictionary for the next round of requests
    file_name_data["file_name"] = None
    file_name_data["json_data"] = None

if __name__ == '__main__':
    app.run(debug=True)
