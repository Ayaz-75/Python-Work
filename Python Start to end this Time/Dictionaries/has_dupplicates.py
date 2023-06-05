old_dictionary = {
    "Names": "Ayaz",
    "Caste": "Lakho",
    "Caste_i": "Lakho"
}
new_dictionary = {}


def has_duplicates(new_dict):
    for item in old_dictionary:
        ite_m = old_dictionary[item]
        if ite_m in new_dict:
            return item

        else:
            new_dict[item] = ite_m

    return new_dict


print(has_duplicates(new_dictionary))
