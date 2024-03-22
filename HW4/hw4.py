import itertools
import json
from HW4 import JSON_FILE_PATH, CSV_FILE_PATH, JSON_RESULT_FILE_PATH
from csv import DictReader


with (open(CSV_FILE_PATH, "r") as books,
      open(JSON_FILE_PATH, "r") as f,
      open(JSON_RESULT_FILE_PATH, "w") as result_json):
    books = DictReader(books)

    users = [
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [],
        }
        for user in json.load(f)
    ]

    for book, user in zip(books, itertools.cycle(users)):
        user["books"].append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"],
            }
        )
        json.dump(users, result_json, indent=4)




