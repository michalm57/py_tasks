# JSON - Java Script Object Notation - small light weigth data format
# Shorter than XML, and quickly parsed by browsers
# json.load(f) - Load JSON data from file
# json.loads(s) - Load JSON data from a string
# json.dump(j, f) - Write JSON data to file
# json.dumps(j) - Output JSON object as string
import json

json_file = open("movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie['title'])
print(movie['actors'])

value = """
            {
                "title": "Tron: Legacy",
                "release_year": 2010,
                "is_awesome": true,
                "won_oscar" : false,
                "actors": null,
                "budget": 170000000
            }
"""

tron = json.loads(value)
print(tron)

json.dumps(movie)
json.dumps(movie, ensure_ascii=False)

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "Jogn Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell"]
movie2["cinematographer"] = "Janusz Kami\u0144ski"

file2 = open("movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close()