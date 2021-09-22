import csv

with open('new_monster.csv', 'r') as monsterDictCSV:
    csv_dict_reader = csv.DictReader(monsterDictCSV)

    for line in csv_dict_reader:
        print(line['monster'])