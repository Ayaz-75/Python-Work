'''
Exercise 143: Anagrams

Two words are anagrams if they contain all of the same letters, but in a different
order. For example, “evil” and “live” are anagrams because each contains one “e”,
one “i”, one “l”, and one “v”. Create a program that reads two strings from the user,
determines whether or not they are anagrams, and reports the result.

'''

# first_string = input("Enter first string: ").lower()
# second_string = input("Enter the second string: ").lower()
# 
# for chars in first_string:
#     if chars in second_string:
#         print(f"{first_string.capitalize()} and {second_string.capitalize()} are Anagrams")
#         break
#     else:
#         print("They are not Anagrams")
#         break



'''
Exercise 144: Anagrams Again

The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored.
Extend your program from Exercise 143 so that it is able to check if two phrases
are anagrams. Your program should ignore capitalization, punctuation marks and
spacing when making the determination.
'''


first_string = input("Enter first string: ").lower()
second_string = input("Enter the second string: ").lower()

# 
for chars in first_string:
    if chars in second_string:
        print(f"{first_string.capitalize()} and {second_string.capitalize()} are Anagrams")
        break
    else:
        print("They are not Anagrams")
        break