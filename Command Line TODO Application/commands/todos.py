from datetime import datetime
import json

def set_list(list_name):
    if list_name == '':
        print('Please select the list before using the current action.')
    return list_name

# Get the desired data from the todo list file 
def get_data(list_file_name):
    with open(f'lists/{list_file_name}', 'r') as json_file:
        data = json.load(json_file)
    return data

# Update the content of the takser file with new data
def update_data(list_file_name, new_data):
    with open(f'lists/{list_file_name}', 'w') as json_file:
        json.dump(new_data, json_file, sort_keys=True, indent=True)

# Add an item to the tasker application
def add_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    title = args[1]
    data = get_data(list_name)
    new_todo = {
        'title' : title,
        'created_at' : datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'completed' : False
    }
    data.append(new_todo)
    update_data(list_name, data)

# Print all the items of the tasker todo list
def show_items(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    data = get_data(list_name)
    complete = 0
    if len(data) == 0:
        print('No items in the tasker app. Add an item rest leave on us.')
    else:
        for index, todo_item in enumerate(data):
            print(index + 1, todo_item['title'])
            if todo_item['completed']:
                complete += 1
        print(f'{complete}/{len(data)} task completed')

# For edit a tasker todo item 
def edit_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    new_title = args[2]
    data = get_data(list_name)
    updated_todo = {
        'title' : new_title,
        'created_at' : datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'completed' : False
    }
    data[item_id - 1] = updated_todo
    update_data(list_name, data)

# Remove a todo item from tasker app
def remove_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data.pop(item_id - 1)
    update_data(list_name, data)

# Mark a todo item as complete in the takser app
def complete_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data[item_id - 1]['completed'] = True
    update_data(list_name, data)

# Mark a todo item as incomplete in the tasker app
def incomplete_item(args):
    list_name = set_list(args[0])
    if not list_name:
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data[item_id - 1]['completed'] = False
    update_data(list_name, data)