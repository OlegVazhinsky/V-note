# import model.py   - it contains all functions for interactions with notes
# import view.py    - it contains all functions for interactions with user
from model import *
from view import *

def init(args):

    # first - create the empty file "notes.csv"
    if not is_file_exists("notes.csv"):
        create_csv_file("notes.csv")
    
    # if there are no arguments
    if (len(args) < 2):
        print_help()
    else:
        # help
        if (args[1] == "help"):
            print_help()
        # add
        elif (args[1] == "add"):
            if is_add_command_ok(args):
                write_note("notes.csv", args)
                print_default_message("Note successfully added.")
            else:
                print_command_error("add")
        # delete
        elif (args[1] == "delete"):
            if is_delete_command_ok(args):
                if delete_note("notes.csv", args):
                    print_default_message("Note successfully deleted.")
                else:
                    print_command_error("delete")
            else:
                print_command_error("delete")
        # edit
        elif (args[1] == "edit"):
            if is_edit_command_ok(args):
                if edit_note("notes.csv", args):
                    print_default_message("Note successfully edited.")
                else:
                    print_command_error("edit")
            else:
                print_command_error("edit")
        # list
        elif (args[1] == "list"):
            if not is_file_exists("notes.csv"):
                print_action_error()
            else:
                read_note("notes.csv")
        # can not identify the command
        else:
            print_error_message(args[1])