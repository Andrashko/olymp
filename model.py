from json import load, dump


FILE_NAME = "./data/todo.json"

todo_list = []


def load_from_file():
    global todo_list
    with open(FILE_NAME, "r") as input_file:
        todo_list = load(input_file)


def save_to_file():
    global todo_list
    with open(FILE_NAME, "w") as output_file:
        dump(todo_list, output_file, indent=4)


def get_todo_list():
    global todo_list
    return todo_list


def add_new_todo(title):
    global id
    new_todo = {
        "id": get_id(),
        "title": title,
        "complete": False
    }
    todo_list.append(new_todo)


def find_todo(id):
    for item in todo_list:
        if item.get("id") == id:
            return item


def delete_todo(id):
    todo = find_todo(id)
    todo_list.remove(todo)
    print(todo_list)


def get_id():
    max_id = max([item["id"] for item in todo_list])
    return max_id+1


def commit():
    save_to_file()


def initialise():
    load_from_file()


initialise()


def count_completed():
    return len([item for item in todo_list if item["complete"]])
