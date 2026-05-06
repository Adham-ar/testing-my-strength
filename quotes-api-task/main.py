import requests
import random
from flask import Flask



def protected(func):
  def wrapper(*args, **kwargs):
      auth_endpoint = "https://api.npoint.io/065565b0103526f8404a"
      quotes_endpoint = "https://api.npoint.io/46926a6b3252cee685b0"
      token = "yoyo"
      headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {token}",
      }
      response = requests.get(auth_endpoint, headers=headers)
      response.raise_for_status()
      auth_data = response.json()

      response = requests.get(quotes_endpoint, headers=headers)
      response.raise_for_status()
      quotes_data = response.json()

      return func(auth_data, quotes_data, *args, **kwargs)
  return wrapper


# auth_endpoint = "https://api.npoint.io/8b99da24accc43184a1a"
# token = "yoyo"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {token}",
# }
# response = requests.get(auth_endpoint, headers=headers)
# print(response.json())


app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Home Page'

@app.route('/quote/random/')
@protected
def random_quote(auth_data, quotes_data):
    select_dict = random.choice(quotes_data)
    random_quote_id = select_dict['id']
    random_quote = select_dict["quote"]


    for author in auth_data:
        if random_quote_id in author['quoteIds']:
            name = author["author"]
            break
        else:
            name = "UNKNOWN NAME"


    print(random_quote)
    return f'<p>Quote Of The Day: {random_quote} BY: {name}</p>'


if __name__ == '__main__':
    app.run(debug=True)