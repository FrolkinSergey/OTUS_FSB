import json
from HW4 import JSON_FILE_PATH, CSV_FILE_PATH
from csv import DictReader

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)


Lst = []
Lst_books = []
for user in users:
    dict_temp = dict()
    dict_temp['name'] = user['name']
    dict_temp['gender'] = user['gender']
    dict_temp['address'] = user['address']
    dict_temp['age'] = user['age']
    dict_temp['books'] = Lst_books
    Lst.append(dict_temp)


while Lst_books:
    for item in Lst_books:
        Lst.append(Lst_books[0])
        Lst_books.pop(0)


with open(CSV_FILE_PATH, newline='') as b:
    reader = DictReader(b)
    for book in reader:
        bookdict = dict()
        bookdict['title'] = book['Title']
        bookdict['author'] = book['Author']
        bookdict['pages'] = book['Pages']
        bookdict['genre'] = book['Genre']
        Lst_books.append(bookdict)


with open("result.json", "w") as f:
    json.dump(Lst, f, indent=4)


