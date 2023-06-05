

print("Welcome to the love clculator !")

name1 = input("Enter your name ?").lower()
name2 = input("Enter their name ?").lower()

combined_string = (name1+name2).lower()


t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t+r+u+e


l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l+o+v+e


score = str(true)+str(love)
print(score)


if int(score) <100 and int(score) > 90:
    print(score,"% You are only made for each other!")

elif int(score) <90 and int(score) > 70:
    print(score,"% You are to good to each other!")

elif int(score)>50 and int(score) < 70:
    print(int(score),"% You are more fiendly with each other!")

elif int(score)<50 and int(score) >0:
    print(int(score),"% You are only okay with each other!")


else:
    print("invalid/unexpected score")




# count_1 = 0
# count_2 = 0

# for letter in truelove:
#     if letter in name1:
#         count_1 += 1

#     if letter in name2:
#         count_2 += 1


# print(f"Your love is: {count_1}{count_2}% you are just okay with each other")

