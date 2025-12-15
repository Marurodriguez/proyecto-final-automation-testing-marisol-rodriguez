import json
import os


def load_users():
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "users.json")

    with open(file_path, "r") as file:
        return json.load(file)
