# # new_dictionary = {}
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
#
# new_dictionary = {'Name': 'Ayaz',
#                   'Caste': 'Lakho'}
#
# print(new_dictionary)
# print(f"Length of first Dictionary = {len(new_dictionary)}")
#
# print(eng2sp)
# print(f"Length of second Dictionary 2 =  {len(eng2sp)}")
#
# print('Caste' in new_dictionary)  # it will give true if key is in the dictionary
# values = new_dictionary.values()
# print('Lakho' in values)
#
#
# def histogram(s):
#     d = {}
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
#
#
# print(histogram('A paragraph is a group of related sentences that support one main idea. In general, paragraphs '
#                 'consist of three parts: the topic sentence, body sentences, and the concluding or the bridge '
#                 'sentence to the next paragraph or section'))
#
#
#
# def count_chars(new_string):
#     new_dictionary = {}
#     for char in new_string:
#         if char not in new_dictionary:
#             new_dictionary[char] = 1
#
#         else:
#             new_dictionary[char] += 1
#
#         print(new_dictionary[char])
#
#     # print(new_dictionary.get('a', 0))
#     return new_dictionary
#
#
# input_string = input("Enter your string here: ")
# print(count_chars(input_string))


# new_dictionary = {}
#
# new_dictionary['name'] = 'Ayaz'
# new_dictionary['caste'] = 'lakho'
# new_dictionary['address'] = 'gambat'
#
# for item in new_dictionary:
#     print(new_dictionary[item])
#

# new_dictionary = {}
#
#
# def is_h(s):
#     for item in s:
#         if item not in new_dictionary:
#             new_dictionary[item] = 1
#
#         else:
#             new_dictionary[item] += 1
#
#     return new_dictionary
#
#
# # input_string = input(": ")  # this will only tell how many times a characters in string has come.
# input_string = input(": ").split(" ")  # this will tell how many times a word has come in a string.
# print(is_h(input_string))

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
