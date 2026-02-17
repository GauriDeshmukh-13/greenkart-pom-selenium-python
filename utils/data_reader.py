import json
import os


def load_test_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "testdata", "products.json")

    with open(file_path) as f:
        data = json.load(f)

    return data
