import csv
import json

movies_dict = {}

# csv class
# extract csv
with open('movie_opinions.csv', newline='', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"')
    # transform csv
    for row in csv_reader:
        person = row[0]
        row.pop(0)
        # transform to json
        movies_dict[person] = {row[i]: float(row[i+1]) for i in range(0, len(row), 2) if row[i] != ''}
        # print(json.dumps(movies_dict, indent=2))