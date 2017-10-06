#! /usr/bin/python3

def team_average(filename):
    try:
        file = open(filename, "r")
        winCount = 0
        gameCount = 0

        for line in file:
            temp = line.split()
            for x in temp:
                if x == 'Win':
                    winCount += 1
            gameCount += 1

        file.close()
        return "{0:.0f}".format(winCount/gameCount*100)
    except IOError as e:
        print("Error: Unable to open "+ filename)

#test
team_average('xxxxxxx')
print(team_average('red_sox.txt'))
