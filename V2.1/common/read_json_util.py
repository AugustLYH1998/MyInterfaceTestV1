import json
from config import BASE_DIR

def read_json_data(pathname):
    path = BASE_DIR+f'\\data\\{pathname}'
    with open(path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        list = []
        for item in json_data:
            list.append(tuple(item.values()))
        return list


if __name__ == '__main__':
    print(read_json_data('login.json'))


# import sys


# print(sys.path)