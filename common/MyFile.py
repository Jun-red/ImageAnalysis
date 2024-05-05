import os
import re

def IsDirExist(directory):
    return True if os.path.exists(directory) else False

def IsFileExist(file):
    return True if os.path.exists(file) else False



def find_all_versions_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        versions = re.findall(r'\[\d+\.\d+\.\d+\]', content)
        return versions
def find_first_versions_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        versions = re.search(r'\[\d+\.\d+\.\d+\]', content)
        return versions.group()
    
