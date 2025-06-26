import json

if __name__ == '__main__':
    # open JSON file in read mode
    with open('data/class_data.json', 'r') as file:
        # load data
        data = json.load(file)
        