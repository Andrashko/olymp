todo_list = [
    {
        "id": 0,
        "title": "Learn python",
        "complete": True
    },
    {
        "id": 1,
        "title": "Relax",
        "complete": False
    }
]

id = len(todo_list)


def add_new_todo(title):
    global id
    new_todo = {
        "id": id,
        "title": title,
        "complete": False
    }
    id += 1
    todo_list.append(new_todo)


def find_todo(id):
    for item in todo_list:
        if item.get("id") == id:
            return item


def delete_todo(id):
    todo = find_todo(id)
    todo_list.remove(todo)
    print(todo_list)


def count_completed():
    return len([item for item in todo_list if item["complete"]])
