import json
import random

with open("./quotes.json", "r") as file:
    quotes = json.load(file)


with open("./authors.json", "r") as file:
    authors = json.load(file)


def gernate_random_quote():
    random_quote = random.choice(quotes)
    for entry in authors:
        # Check if the target quote_id is in the current author's quoteIds list
        if random_quote["id"] in entry["quoteIds"]:
            return {
                "quoteId": random_quote["id"],
                "quote": random_quote["quote"],
                "author": entry["author"],
            }
