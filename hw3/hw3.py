#! /usr/bin/python3

#reads in class data from a file and creates a dictionary 
#prints the data from the dictionary

#returns a dictionary created from file
def class_tuple_create(filename):
    try:
        file = open(filename, 'r')
    except:
        print ('CANNOT OPEN', filename)
    else:
        data = {}
        for line in file:
            data_list = line.split()
            course_id = data_list[0]
            room_num = data_list[1]
            instr = data_list[2]
            start_time = data_list[3]
            class_tuple = (room_num, instr, start_time)
            data[course_id] = class_tuple
        return data

#prints the data for each class in alphabetical order
def print_classes(class_info):
    class_ids = []

    for class_id in class_info:
        class_ids.append(class_id)

    class_ids.sort()

    print("ID   Room    Instr   Start")
    print("-------------------------------")
    for class_id in class_ids:
        print(class_id + "  " + class_info[class_id][0] + 
                "   " + class_info[class_id][1] + "     " + 
                class_info[class_id][2])

#test
class_information = class_tuple_create('xxxxx')
class_information = class_tuple_create('courses.txt')
print_classes(class_information)
