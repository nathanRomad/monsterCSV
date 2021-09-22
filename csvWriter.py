import csv

with open("monster.csv", 'r') as monster_csv:
    csv_reader = csv.reader(monster_csv)

    with open('new_monster.csv', 'w') as new_monster_csv:
        csv_writer = csv.writer(new_monster_csv)

        for line in csv_reader:
            csv_writer.writerow(line)