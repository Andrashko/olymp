from flask import Flask, render_template, request, redirect, url_for
from model import commit, get_todo_list, add_new_todo, count_completed, find_todo, delete_todo


app = Flask(__name__)


@app.route("/")
def home():
    todo_list = get_todo_list()
    return render_template(
        "todo.html",
        todo_list=todo_list
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
    return "Add author page here"


@app.route("/mark_all_done")
def mark_all_done():
    pass


if __name__ == "__main__":
    app.run(debug=True)
