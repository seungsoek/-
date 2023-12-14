import csv
with open('./data/team_stats.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        print(i+1, row['common_name'])

with open('./data/player_stats.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        
        print(i+1, row['full_name'])
