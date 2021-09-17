import csv

with open('monster.csv', 'r') as monsterCSV:
    monsterReader = csv.reader(monsterCSV)

    for line in monsterReader:
        print(line)
