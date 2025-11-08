from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Welcome to CI/CD with Flask!")

@app.route("/square/<int:number>")
def square(number):
    result = number * number
    return jsonify(number=number, square=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
# To run the app, use the command: python app.py