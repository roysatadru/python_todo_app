user_prompt: str = "Enter a todo: "

todos: list = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(f"Added {todo}. List has {len(todos)} items.")
