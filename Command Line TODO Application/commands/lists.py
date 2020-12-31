from datetime import datetime
import os.path
import json

FILE_NAME = 'lists.json'

def show_lists(args):
    with open(FILE_NAME, 'r') as lists_json:
        try:
            data = json.load(lists_json)
            for index, todo_list in enumerate(data.keys()):
                print(index + 1, data[todo_list]['title'])
        except:
            print('Some error occured while creating the todo task.')

def use_list(args):
    list_name = args[0]
    with open(FILE_NAME, 'r') as lists_json:
        try:
            data = json.load(lists_json)
            if (data.get(list_name)):
                return f'{list_name}.json'
            else:
                return -1
        except:
            print('Some error occured while creating the todo task.')

def create_list(args):
    list_name = args[0]
    new_list = {}
    with open(FILE_NAME, 'r+') as lists_json:
        try:
            data = json.load(lists_json)
            if (data.get(list_name)):
                print(f'The list with the current name {list_name} is already exists. Please try a different name.')
            else:
                new_list = {
                    'title' : list_name,
                    'created_at' : datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                }
                data[list_name] = new_list
                with open(f'lists/{list_name}.json', 'w') as new_list:
                    new_list.write('[\n]')
                    print(f'{list_name} created successfully.')
                lists_json.seek(0)
                json.dump(data, lists_json, sort_keys=True, indent=True)
        except:
            print('Some error occured while creating the todo list.')