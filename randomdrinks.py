import json
import random
import azure.functions as func

def random_drink():
    drinks = ["coffee", "tea", "beer", "wine", "water", "juice"]
    return random.choice(drinks)

def main(req: func.HttpRequest) -> func.HttpResponse:
    drink = random_drink()
    message = f"You should drink some {drink}"

    return func.HttpResponse(
        json.dumps({"message": message, "drink": drink}),
        mimetype="application/json",
        status_code=200
    )
