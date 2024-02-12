import time
import functions

now = time.strftime("%b %d, %Y - %H:%M:%S")
print("It is ", now)


text = """
Welcome to ToDo App
Author: Adam Abdi
Copyright © 2024
"""
print(text)


todos = []


while True:
    # Get user input and strip space characters from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # Check if user action is "add"
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):  # | 'display'
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"\nThis todos '{todo_to_remove}' was removed from the list successfully.\n"
            print(message)
        except IndexError:
            print("There is no item with that number. list index out of range.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print('+-' * 28)
        print("\nInvalid command.")
        print('+-' * 28)

print("Bye!")
