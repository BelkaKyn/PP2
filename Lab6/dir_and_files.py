1.
import os

def list_directories_and_files(path):
    try:
        if not os.path.exists(path):
            print("The specified path does not exist.")
            return
        
        directories = []
        files = []
        
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                directories.append(item)
            elif os.path.isfile(full_path):
                files.append(item)
        
        print("Directories:")
        for directory in directories:
            print(directory)
        
        print("\nFiles:")
        for file in files:
            print(file)
    
    except Exception as e:
        print("An error occurred:", e)

path = "/path/to/your/directory"

list_directories_and_files(path)

2.
import os

def check_access(path):
    try:
        if not os.path.exists(path):
            print(f"The specified path '{path}' does not exist.")
            return
        
        if os.access(path, os.R_OK):
            print(f"Read access to '{path}' is permitted.")
        else:
            print(f"No read access to '{path}'.")
        
        if os.access(path, os.W_OK):
            print(f"Write access to '{path}' is permitted.")
        else:
            print(f"No write access to '{path}'.")
        
        if os.access(path, os.X_OK):
            print(f"Execute access to '{path}' is permitted.")
        else:
            print(f"No execute access to '{path}'.")
        
    except Exception as e:
        print("An error occurred:", e)

path = "/path/to/your/file_or_directory"

check_access(path)

3.
import os

def check_path(path):
    try:
        if not os.path.exists(path):
            print(f"The specified path '{path}' does not exist.")
            return
        
        directory, filename = os.path.split(path)
        
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
        
    except Exception as e:
        print("An error occurred:", e)

path = "/path/to/your/file_or_directory"

check_path(path)

4.
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"The number of lines in the file '{file_path}' is: {line_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)

file_path = "path/to/your/text_file.txt"

count_lines(file_path)
5.
def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List successfully written to file '{file_path}'.")
    except Exception as e:
        print("An error occurred:", e)

file_path = "path/to/your/output_file.txt"

data = [1, 2, 3, 4, 5]

write_list_to_file(file_path, data)

6.
import string

def generate_text_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = f"{letter}.txt"
            with open(file_name, 'w') as file:
                file.write(f"This is file {file_name}.\n")
        print("Text files successfully generated.")
    except Exception as e:
        print("An error occurred:", e)

generate_text_files()
7.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print("An error occurred:", e)

source_file = "path/to/your/source_file.txt"
destination_file = "path/to/your/destination_file.txt"

copy_file(source_file, destination_file)

8.
import os

def delete_file(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"The specified path '{file_path}' does not exist.")
            return
        
        if not os.access(file_path, os.W_OK):
            print(f"No write access to '{file_path}', unable to delete the file.")
            return
        
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)

file_path = "path/to/your/file_to_delete.txt"

delete_file(file_path)


