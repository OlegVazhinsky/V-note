def print_help():
    print("-------- Program v-notes --------")
    print("Program helps you to create notes in commandline way.")
    print("It uses the following sintax:")
    print('add -title "NOTE_TITLE" -note "NOTE_TEXT"')

def print_error_message(command):
    print("You used argument '" + command + "', I can not undertand it.")
    print("Please, check youself and try again.")
    print("You can also use 'help' argument to see all commands.")
    