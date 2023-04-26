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
    file.close()

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
    file.close()

def write_note(file_path, note):
    if os.stat(file_path).st_size > 0:
        with open(file_path, 'r') as file:
            id = len(file.readlines()) + 1
        file.close()
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
    file.close()

def is_add_command_ok(args):
    result_dict = {}
    for c in ["add","-title","-text"]:
        for i in range(len(args)):
            if c == args[i]:
                result_dict[c] = i
                break
    if result_dict["add"] == 1 and result_dict["-title"] == 2 and result_dict["-text"] > 3:
        return True
    else:
        return False

