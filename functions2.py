def shutdown(command):
    if command == "Yes":
        return "Shutting down"
    elif command == "No":
        return "Abort shut down"
    else:
        return "Sorry"

user_input = input("Enter Yes or No: ")
print(shutdown(user_input))