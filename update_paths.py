import os
import fileinput
import sys

def update_imports(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                update_file(filepath)

def update_file(filepath):
    with fileinput.FileInput(filepath, inplace=True) as file:
        for line in file:
            # Replace 'from tonic.tonic import' with 'from tonic.tonic.tonic.tonic import'
            print(line.replace('tonic.tonic', 'tonic.tonic.tonic.tonic'), end='')

repo_directory = "/Users/gayathrianant/agv/mlrc/tonic.tonic"
update_imports(repo_directory)