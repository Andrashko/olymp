from flask import Flask, render_template, request, redirect, url_for
from model import commit, get_todo_list, add_new_todo, count_completed, find_todo, delete_todo


app = Flask(__name__)


@app.route("/")
def home():
    todo_list = get_todo_list()

    completed = 0
    for todo in todo_list:
        if todo["complete"]:
            completed = completed + 1

    return render_template(
        "base.html",
        todo_list=todo_list,
        completed=completed
    )


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    add_new_todo(title)
    commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = find_todo(todo_id)
    todo["complete"] = not todo["complete"]
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    delete_todo(todo_id)
    commit()
    return redirect(url_for("home"))


@app.route("/author")
def author():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
