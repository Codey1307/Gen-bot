import random

from utils.json_loader import load_json


CITIES_FILE = "data/cities.json"
BLACKLIST_FILE = "data/blacklist.json"


def generate_cities(amount):

    cities = load_json(CITIES_FILE)

    blacklist = load_json(BLACKLIST_FILE)

    blacklist = {
        city.lower()
        for city in blacklist
    }

    available = [

        city

        for city in cities

        if city["name"].lower() not in blacklist

    ]

    amount = min(
        amount,
        len(available)
    )

    return random.sample(
        available,
        amount
    )