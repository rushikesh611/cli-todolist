import json
from datetime import datetime
import sys

def get_data(list_name):
    data=[]
    with open(list_name,'r+') as todo_list:
        data = json.load(todo_list)
    return data

def update_data(list_name, new_data):
    with open(list_name,'w') as json_file:
        json.dump(new_data, json_file, sort_keys=True, indent=True)


def add_item(args):
    data = get_data('lists.json')
    title = args[0]
    data.append({
        'title': title,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'completed': False
    })
    with open('lists.json','w') as todo_list:
        json.dump(data,todo_list, sort_keys=True, indent=True)
    print("Task added")

def show_items(args):
    data = get_data('lists.json')
    if len(data)==0:
        print('No Item in the list')
        return
    completed=0
    for index, todo_item in enumerate(data):
        print(index + 1, todo_item['title'])

def remove_item(args):
    item_id = int(args[0])
    data = get_data('lists.json')
    data.pop(item_id - 1)
    update_data('lists.json',data)
    print('Deleted todo #',item_id)


def done(args):
    item_id = int(args[0])
    data = get_data('lists.json')
    data[item_id-1]['completed']=True
    update_data('lists.json',data)
    print('Marked as done!')

def report(args):
    data = get_data('lists.json')
    completed=0
    print('Remaining Tasks')
    for index, todo_item in enumerate(data):
        print(index + 1, todo_item['title'])
        if(todo_item['completed']==True):
            completed += 1
    print(f'{completed}/{len(data)} tasks completed.')
    print(f'{len(data)-completed} tasks pending.')
