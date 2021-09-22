import csv
from os import times

with open('monster.csv', 'r') as monsterCSV:
    monsterReader = csv.reader(monsterCSV)

    # next(monsterReader)

    for line in monsterReader:
        timestamp = line[0]
        researcher = line[1]
        monster = line[2]
        latitude = line[3]
        longitude = line[4]

        # print(timestamp)
        # print(researcher)
        # print(monster)
        # print(latitude)
        # print(longitude)

        print(line)