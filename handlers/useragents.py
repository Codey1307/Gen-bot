import random

from utils.json_loader import load_json


def generate_useragents(source: str, amount: int):

    file_path = f"data/{source}.json"

    useragents = load_json(file_path)

    amount = min(amount, len(useragents))

    return random.sample(useragents, amount)