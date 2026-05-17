import datetime

import pandas as pd
from data import gernate_random_quote
from flask import Flask, jsonify, request

EXPECTED_TOKEN = "DEMO_AUTH@2022"


def require_token(f):

    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return (
                jsonify({"message": "You are not authorized to use this API!"}),
                403,
            )

        token = auth_header.split(" ")[1]

        if token != EXPECTED_TOKEN:
            return (
                jsonify({"message": "You are not authorized to use this API!"}),
                403,
            )

        return f(*args, **kwargs)

    return decorated_function


app = Flask(__name__)

track_list = []


@app.route("/")
def hello_world():
    return f"Home Page"


def api_calls():
    total_calls = sum([item["count"] for item in track_list])

    if total_calls > 0 and total_calls % 10 == 0:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"quotes_api_report_{time_now}.csv"

        df = pd.DataFrame(track_list)
        df.columns = ["Quote ID", "Count"]
        df.to_csv(filename, index=False)


@app.route("/quote/random/")
@require_token
def random_quote():

    print(request.get_json())

    api_calls()
    respond = jsonify(gernate_random_quote())

    return respond


if __name__ == "__main__":
    app.run(debug=True)
