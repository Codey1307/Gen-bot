import random

from utils.json_loader import load_json


SURNAMES_FILE = "data/surnames.json"


def generate_surnames(amount: int):

    surnames = load_json(SURNAMES_FILE)

    amount = min(amount, len(surnames))

    return random.sample(surnames, amount)