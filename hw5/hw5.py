#! /usr/bin/python3

# Reads in text files and creates a set of words in each file
# Creates sets of the words found in one file but not the other
# Prints the difference sets found

# reads in a text file and returns a set of all words found in the file
def word_set_create(filename):
    word_set = set()
    try:
        file = open(filename, 'r')
    except:
        print('COULD NOT OPEN', filename)
    else:
        for line in file:
            for word in line.split():
                word = word.lower() 
                if word not in word_set:
                    word_set.add(word)
        return word_set

# create a list of all words found in the first set that were not found in 
# the second.
def set_difference(set_1, set_2):
    return set_1.difference(set_2)

# prints the words in a set alphabetical order
def word_set_print(word_set):
    for word in sorted(word_set):
        print(word)

# TEST
print()
word_set = word_set_create('xxxxxxx')
word_set_1 = word_set_create('gettysburg.txt')
word_set_2 = word_set_create('gettysburg_hay.txt')
set_1_set_2_difference = set_difference(word_set_1, word_set_2)
set_2_set_1_difference = set_difference(word_set_2, word_set_1)

print()
print('Words in the first text not found in the second:')
word_set_print(set_1_set_2_difference)
print()
print('Words in the second text not found in the first:')
word_set_print(set_2_set_1_difference)
print()
