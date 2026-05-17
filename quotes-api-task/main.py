
from data import generate_random_quote
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
                404,
            )

        return f(*args, **kwargs)

    return decorated_function


app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Home Page"


@app.route("/quote/random/", methods=["GET", "POST"])
@require_token
def random_quote():
    print(request.get_json())
    respond = jsonify(generate_random_quote()), 200
    return respond


if __name__ == "__main__":
    app.run(debug=True)
