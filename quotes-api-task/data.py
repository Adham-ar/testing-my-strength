import json
import random
import pandas as pd
from datetime import datetime

with open("./quotes.json", "r") as file:
    quotes = json.load(file)


with open("./authors.json", "r") as file:
    authors = json.load(file)


quote_counter = {}
TOTAL_CALLS = 0

def generate_random_quote():
    global quote_counter, TOTAL_CALLS
    random_quote = random.choice(quotes)
    for entry in authors:
        # Check if the target quote_id is in the current author's quoteIds list
        if random_quote["id"] in entry["quoteIds"]:

            quote_id = random_quote["id"]
            if quote_id not in quote_counter:
                quote_counter[quote_id] = 0

            quote_counter[quote_id] += 1

            TOTAL_CALLS = sum(quote_counter.values())

            if TOTAL_CALLS >= 10:
                report()

            print(quote_counter)
            print(TOTAL_CALLS)

            return {
                "quoteId": random_quote["id"],
                "quote": random_quote["quote"],
                "author": entry["author"],
            }

def report():
    global quote_counter, TOTAL_CALLS

    df = pd.DataFrame(list(quote_counter.items()), columns=["Quote ID", "Count"])
    df = df.sort_values(by="Count", ascending=False)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    excel_file = f"quotes_api_report_{timestamp}.xlsx"
    df.to_excel(excel_file, index=False, sheet_name="Quotes Report")

    print(f"Success! A 100+ calls threshold report was saved as: {excel_file}")

    TOTAL_CALLS = 0
    quote_counter = {}

