from model import *
from view import *

def init(args):
    if (len(args) < 2):
        print_help()
    else:
        if (args[1] == "help"):
            print_help()
        elif (args[1] == "add"):
            print_default_message("Function is in progress")
            create_csv_file("notes.csv")
        elif (args[1] == "delete"):
            print_default_message("Function is in progress")
        elif (args[1] == "edit"):
            print_default_message("Function is in progress")
        elif (args[1] == "list"):
            print_default_message("Function is in progress")
        else:
            print_error_message(args[1])