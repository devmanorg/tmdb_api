import json
import os

def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        films_data = json.load(my_file)
        return films_data
