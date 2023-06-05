travel_log = [
    {
        "Province": "Sindh",
        'cities': ['Karachi', 'Hyderabad', 'Sukkur', 'Gambat'],
        'times_visited': 4
    },

    {
        "Province": "Baluchistan",
        'cities': ['Quetta', 'Second_quetta', 'Third_quetta'],
        'times_visited': 1
    },

    {
        "Province": "Punjab",
        'cities': ['Islamabad', 'Lahore', 'Pindi'],
        'times_visited': 5
    }
]


# print(travel_log[1])
new_dict = {
                "Country": "Russia",
                'cities': ['Moscow', 'Saint', 'petersburg'],
                'times_visited': 3
            }

travel_log.append(new_dict)

print(travel_log)
