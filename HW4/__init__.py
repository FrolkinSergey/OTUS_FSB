import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="files/books.csv")
JSON_FILE_PATH = get_path(filename="files/users.json")
RESULT_JSON_FILE_PATH = get_path(filename="result.json")