from model import *
from view import *

def init(args):
    if not is_file_exists("notes.csv"):
        create_csv_file("notes.csv")
    if (len(args) < 2):
        print_help()
    else:
        if (args[1] == "help"):
            print_help()
        elif (args[1] == "add"):
            if is_add_command_ok(args):
                write_note("notes.csv", args)
                print_default_message("Note successfully added.")
            else:
                print_command_error("add")
        elif (args[1] == "delete"):
            if not is_file_exists("notes.csv"):
                print_action_error("delete")
        elif (args[1] == "edit"):
            print_default_message("Function is in progress")
        elif (args[1] == "list"):
            if not is_file_exists("notes.csv"):
                print_action_error("see")
            else:
                read_note("notes.csv")
        else:
            print_error_message(args[1])