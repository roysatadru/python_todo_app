todos: list[str] = []

while True:
    user_action = input("Add, edit, show or exit todos? ")
    user_action = user_action.lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a new todo: ")
            todos.append(todo)
        case "edit":
            todo_index = int(input("Enter the index of the todo to edit: "))
            todo_index -= 1
            new_todo = input("Enter the new todo: ")
            todos[todo_index] = new_todo
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            break

print("Goodbye!")
