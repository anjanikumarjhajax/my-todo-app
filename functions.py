FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as local_file:
        content = local_file.readlines()
    return content


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
