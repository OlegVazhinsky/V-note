def print_help():
    print("-------- Program v-notes --------")
    print("Program helps you to create and edit notes in commandline.")
    print("It uses the following sintax:\n")
    print("- to add note use:")
    print('add -title "NOTE_TITLE" -text "NOTE_TEXT"\n')
    print("- to show the list of all notes use:")
    print('list\n')
    print("- to delete note use:")
    print('delete -id "NOTE_ID"\n')
    print("- to edit note use:")
    print('edit -id "NOTE_ID" -title "NOTE_TITLE" -text "NOTE_TEXT"\n')
    print("If you find any bugs or you have any suggestions, please e-mail: oleg_vazhinsky92@mail.ru")

def print_error_message(command):
    print("You used argument '" + command + "', I can not undertand it.")
    print("Please, check youself and try again.")
    print("You can also use 'help' argument to see all commands.")

def print_action_error(action):
    print("You tried to " + action + " note(s), but non of them has been created.")

def print_default_message(message):
    print(message)

def print_command_error(command):
    print("Something went wrong with command '" + command + "'.")
    print("Please, check youself and try again.")