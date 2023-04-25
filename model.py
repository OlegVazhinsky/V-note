import os.path
import csv

def create_csv_file(file_name):
    if (not os.path.exists(file_name)):
        with open(file_name, 'w') as file:
            csv.writer(file)
    #else:
    #    print("File is already exists.")

def read_note_from_file(note_id):
    
    print()