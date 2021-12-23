import csv

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

with open('topmovies.csv', newline="") as f:
  reader = csv.reader(f)
  data = list(reader)


@app.route("/moviedata")
def function1():
    return jsonify({
         'data': data,
         'status':'success'

    })



if __name__ == "__main__":
    app.run()