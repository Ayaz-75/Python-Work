# welcome to the nesting dictionary program
travel_log = [
    {"Country": "France",
     "no_of_visits": 12,
     "cities_visited": ["paris", "lille", "dijon"],
     },

    {"Country": "Germany",
     "no_of_visits": 10,
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     }
]


def add_new_country(country_visited, visits_times, cities_visited):
    new_country ={}
    new_country["Country"] = country_visited
    new_country["no_of_visits"] = visits_times
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint petersburg"])

print(travel_log)
