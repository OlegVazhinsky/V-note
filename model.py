# standard imports.
import os.path
import csv
import datetime

# check if file exists. return True if the file exists. False otherwise.
def is_file_exists(file_path):
    if (not os.path.exists(file_path)):
        return False
    else:
        return True

# creates file.
def create_csv_file(file_path):
    with open(file_path, 'w') as file:
        csv.writer(file)

# read notes. returns the list of notes.
def read_note(file_path):
    notes = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for note in reader:
            notes.append(note)
    return notes

# writes note to the file.
def write_note(file_path, note):
    if os.stat(file_path).st_size > 0:
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=";")
            id = 1
            for item in reader:
                if int(item[0]) > id:
                    id = int(item[0]) + 1
    else:
        id = 1
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for i in range(len(note)):
            if "-text" == note[i]:
                index = i
        result_note = []
        result_note.append(id)
        title = ""
        for i in range(3, index):
            title = title + note[i] + " "
        title = title[:-1]
        text = ""
        for i in range(index + 1, len(note)):
            text = text + note[i] + " "
        text = text[:-1]
        result_note.append(title)
        result_note.append(text)
        result_note.append(datetime.datetime.now().strftime("%H:%M:%S"))
        result_note.append(datetime.date.today().strftime("%d %b %Y"))
        writer.writerow(result_note)

# deletes the note. Returns True if success. False otherwise.
def delete_note(file_path, args):
    if args[3].isdigit():
        id = int(args[3])
    else:
        return False
    flag = False
    with open(file_path, 'r') as file_read:
        reader = csv.reader(file_read, delimiter=";")
        for note in reader:
            if int(note[0]) == id:
                flag = True
    notes = []
    with open(file_path, 'r') as file_read:
        reader = csv.reader(file_read, delimiter=";")
        for note in reader:
            if int(note[0]) != id:
                notes.append(note)
    if flag == True:
        create_csv_file(file_path)
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            for note in notes:
                writer.writerow(note)
        return True
    else:
        return False

# edites the note. Returns True if success. False otherwise.
def edit_note(file_path, args):
    if args[3].isdigit():
        id = int(args[3])
    else:
        return False
    flag = False
    with open(file_path, 'r') as file_read:
        reader = csv.reader(file_read, delimiter=";")
        for note in reader:
            if int(note[0]) == id:
                flag = True
    notes = []
    with open(file_path, 'r') as file_read:
        reader = csv.reader(file_read, delimiter=";")
        for note in reader:
            if int(note[0]) != id:
                notes.append(note)
            else:
                for i in range(len(args)):
                    if args[i] == "-text":
                        index = i
                result_note = []
                result_note.append(id)
                title = ""
                for i in range(5, index):
                    title = title + args[i] + " "
                title = title[:-1]
                text = ""
                for i in range(index + 1, len(args)):
                    text = text + args[i] + " "
                text = text[:-1]
                result_note.append(title)
                result_note.append(text)
                result_note.append(datetime.datetime.now().strftime("%H:%M:%S"))
                result_note.append(datetime.date.today().strftime("%d %b %Y"))
                notes.append(result_note)
    if flag == True:
        create_csv_file(file_path)
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            for note in notes:
                writer.writerow(note)
        return True
    else:
        return False

# checks if user wrote "add" command correctly. Returns True if success. False otherwise.
def is_add_command_ok(args):
    result_dict = {}
    for c in ["add","-title","-text"]:
        for i in range(len(args)):
            if c == args[i]:
                result_dict[c] = i
                break
    if len(result_dict) == 3:
        if result_dict["add"] == 1 and result_dict["-title"] == 2 and result_dict["-text"] > 3:
            return True
    else:
        return False
    
# checks if user wrote "delete" command correctly. Returns True if success. False otherwise.
def is_delete_command_ok(args):
    result_dict = {}
    for c in ["delete","-id"]:
        for i in range(len(args)):
            if c == args[i]:
                result_dict[c] = i
                break
    if len(result_dict) == 2:
        if result_dict["delete"] == 1 and result_dict["-id"] == 2 and len(args) == 4:
            return True
        else:
            return False
    else:
        return False
    
# checks if user wrote "edit" command correctly. Returns True if success. False otherwise.
def is_edit_command_ok(args):
    result_dict = {}
    for c in ["edit","-id","-title","-text"]:
        for i in range(len(args)):
            if c == args[i]:
                result_dict[c] = i
                break
    if len(result_dict) == 4:
        if result_dict["edit"] == 1 and result_dict["-id"] == 2 and result_dict["-title"] == 4 and result_dict["-text"] > 5:
            return True
        else:
            return False
    else:
        return False