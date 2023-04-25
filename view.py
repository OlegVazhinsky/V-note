def print_help():
    print("-------- Program v-notes --------")
    print("Program helps you to create and edit notes in commandline.")
    print("It uses the following sintax:\n")
    print("- to add note use:")
    print('add -title "NOTE_TITLE" -note "NOTE_TEXT"\n')
    #print("- if you want to add note and encrypt it your note with the key, please use:")
    #print('add -title "NOTE_TITLE" -note "NOTE_TEXT" -key "YOUR_KEY"')
    #print("* Please, try not to forget it, otherwise your note will be lost or hardly decrypted.")
    print("- to show the list of all notes use:")
    print('list\n')
    print("- to delete note use:")
    print('delete -id "NOTE_ID"\n')
    #print("- if note that should be deleted is encrypted you should use:")
    #print('delete -id "NOTE_ID" -key "YOUR_KEY"')
    print("- to edit note use:")
    print('edit -id "NOTE_ID"\n')
    #print("- if note that should be edited is encrypted you should use:")
    #print('edit -id "NOTE_ID" -key "YOUR_KEY"')
    print("If you find any bugs or you have any suggestions, please e-mail: oleg_vazhinsky92@mail.ru")

def print_error_message(command):
    print("You used argument '" + command + "', I can not undertand it.")
    print("Please, check youself and try again.")
    print("You can also use 'help' argument to see all commands.")

def print_default_message(message):
    print(message)