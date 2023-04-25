from model import *
from view import *

def init(args):
    if (len(args) < 2):
        print_help()
    else:
        if (args[1] == "help"):
            print_help()
        elif (args[1] == "add"):
            command = "add"
        elif (args[1] == "delete"):
            command = "delete"
        elif (args[1] == "edit"):
            command = "edit"
        elif (args[1] == "list"):
            command = "list"
        else:
            print_error_message(args[1])