import csv
import requests
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

headers = {"x-locale":"pl_PL", "content-type":"application/json"}
# load csv
for key in movies_dict:
    for movie_title in movies_dict[key]:
        movie_title = requests.utils.quote(movie_title)
        req_movie_search = requests.get("https://www.filmweb.pl/api/v1/live/search?query=" 
                                        + movie_title + "&pageSize=1", headers=headers)
        resp_movie_search = req_movie_search.json()
        movie_id = resp_movie_search["searchHits"][0]["id"]
        print(movie_id)
        req_movie_info = requests.get('https://www.filmweb.pl/api/v1/title/' + str(movie_id) + '/info',
                              headers=headers)
        resp_movie_info = req_movie_info.json()
        print(resp_movie_info)
        if "originalTitle" in resp_movie_info:
            if movie_title != resp_movie_info["originalTitle"]:
                movies_dict[key] = resp_movie_info["originalTitle"]
                print(movies_dict[key])
