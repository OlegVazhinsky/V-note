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
            if is_delete_command_ok(args):
                if delete_note("notes.csv", args):
                    print_default_message("Note successfully deleted.")
                else:
                    print_command_error("delete")
            else:
                print_command_error("delete")
        elif (args[1] == "edit"):
            if is_edit_command_ok(args):
                if edit_note("notes.csv", args):
                    print_default_message("Note successfully edited.")
                else:
                    print_command_error("edit")
            else:
                print_command_error("edit")
        elif (args[1] == "list"):
            if not is_file_exists("notes.csv"):
                print_action_error("see")
            else:
                read_note("notes.csv")
        else:
            print_error_message(args[1])