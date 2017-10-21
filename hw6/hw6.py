#! /usr/bin/python3

#create a dictionary whose keys are all the directories listed in the PATH
#system variable, and whose values are the number of files in each of these 
#directories
#print each directory entry sorted by directory name.

import os
import os.path

#accept a shell variable as its only parameter
#return the value of this shell variable
#return empty string if variable undefined
def get_environment_variable_value(variable_name):
    try:
        var_value = os.environ[variable_name]
    except:
        return 
    else:
        return var_value

#accept no parameters
#returns a list of the directories contained in 'PATH'
def get_dirs_from_path():
    dirs = get_environment_variable_value('PATH')
    dir_list = []
    for direct in dirs.split(':'):
        dir_list.append(direct)
    return dir_list

#accept a directory name as a parameter
#return the number of files in this directory not counting sub-directories
def get_file_count(dir_path):
    file_list = []
    if os.path.isdir(dir_path):
        for item in os.listdir(dir_path):
            if not os.path.isdir(os.path.join(dir_path, item)):
                file_list.append(item)
        return len(file_list)
    else:
        return 0

#accept a list of directories as its only parameter
#return a dictionary in form directory names : number of files in each 
#directory
def get_file_count_for_dir_list(dir_list):
    file_count_dict = {}
    for direct in dir_list:
        file_count_dict[direct] = get_file_count(direct)
    return file_count_dict

#accept a dictionary as its only parameter
#print out the key and the value for each directory entry 
#on a single line of output
#printed sorted by their key
def print_sorted_dictionary(dict):
    for key in sorted(dict):
        print(key, dict[key])

#TESTS
path_dirs = get_dirs_from_path()
dir_count = get_file_count_for_dir_list(path_dirs)
print_sorted_dictionary(dir_count)
