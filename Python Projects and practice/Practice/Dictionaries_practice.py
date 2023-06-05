"""Dictionary practice"""

'''def check_dict(diction):
    if diction == {}:
        return True
    else:
        return False


programming_dictionary = {
    "Name": "Ayaz",
    "Caste": "Lakho",
    "City": "Gambat"
}

new_dict = {}


print(programming_dictionary)
# print(check_dict(programming_dictionary))
# print(check_dict(new_dict))

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])'''

'''marks_dict = {
    "Aaqib": 85,
    "Ayoob": 95,
    "Ayaz": 75
}

new_dict = {}

for score in marks_dict:
    new_dict[score] = marks_dict[score]
    if 91 < marks_dict[score] <= 100:
        new_dict[score] = "Outstanding"

    if 81 < marks_dict[score] <= 90:
        new_dict[score] = "Exceeds Expectations"

    if 71 < marks_dict[score] <= 80:
        new_dict[score] = "Acceptable"

print(new_dict)'''

# -------------------------- Nested Dictionary ----------------------------
travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "lille", "Dijon"],
     "number_visits": 12
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Strutt_grate"],
     "number_visits": 8
     },
]


def add_new_country(country_v, cities_visited, times_visited):
    new_country = {}

    new_country["country"] = country_v
    new_country["cities_visited"] = cities_visited
    new_country["number_visits"] = times_visited

    travel_log.append(new_country)


add_new_country("Russia", ["Moscow", "saintbergs"], 2)

print(f"{travel_log}")
