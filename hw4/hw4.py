#! /usr/bin/python3

#reads in a text file
#create a dictionary of word frequencies 
#prints a sorted list of all words in the file and their frequency

#read in a text file and return a word frequency dictionary
def word_frequencies_create(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Cannot open', filename)
    else:
        dict = {}
        for line in file:
            for word in line.split():
                word = word.lower()
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] = dict[word] + 1
        return dict

#print the words in alphabetical order along with the number of times each 
#word appears in the file
def word_frequency_print(frequencies):
    for key in sorted(frequencies):
        print(key, frequencies[key])

#TEST
word_freq = word_frequencies_create('xxxxxxx')
word_freq = word_frequencies_create('gettysburg.txt')
word_frequency_print(word_freq)


