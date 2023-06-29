from flask import Flask, render_template, request, redirect, url_for


# models
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

# app


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html",
                           todo_list=todo_list,
                           completed_count=count_completed()
                           )


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    add_new_todo(title)
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = find_todo(todo_id)
    todo["complete"] = not todo["complete"]
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for("home"))


@app.route("/author")
def author():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)


