import os.path
import csv
import datetime

def is_file_exists(file_path):
    if (not os.path.exists(file_path)):
        return False
    else:
        return True

def create_csv_file(file_path):
    with open(file_path, 'w') as file:
        csv.writer(file)

def read_note(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for note in reader:
            print("_________________")
            print("ID = " + note[0])
            print("Title = " + note[1])
            print("Text = " + note[2])
            print("Time = " + note[3])
            print("Date = " + note[4])

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
        text = ""
        for i in range(index + 1, len(note)):
            text = text + note[i] + " "
        result_note.append(title)
        result_note.append(text)
        result_note.append(datetime.datetime.now().strftime("%H:%M:%S"))
        result_note.append(datetime.date.today().strftime("%d %b %Y"))
        writer.writerow(result_note)

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
                text = ""
                for i in range(index + 1, len(args)):
                    text = text + args[i] + " "
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