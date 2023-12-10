from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/retrieve")
def retrieve():
    try:
        result = subprocess.check_output(["python", "read.py"])
        print(jsonify(result))
        return jsonify(result)
    except subprocess.CalledProcessError as e:
        return f"Error with msg: {e.output}"
    
if __name__ == "__main__":
    app.run(debug=True)
