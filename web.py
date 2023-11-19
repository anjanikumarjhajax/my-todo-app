import streamlit as sl
import functions


def add_todo():
    todos1 = functions.get_todos()
    todo1 = sl.session_state["new_todo"] + "\n"
    todos1.append(todo1)
    functions.write_todos(todos1)
    print(todo1)


todos = functions.get_todos()
print(type(todos))

sl.title("My Todo App")
sl.subheader("This is my todo app")
sl.write("This app is to improve productivity")

# sl.checkbox("Buy grocery")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

# sl.text_input("")
sl.text_input(label="", placeholder="add new todo..",
              on_change=add_todo, key="new_todo")

sl.session_state




