from appartment import Apartment

'''
Exercise 2:
Open a new python file named with your student ID and import the class you have created 
in Exercise 1 and Create 7 instances of Apartment class with the following information:
Instance 1 : (RoomsNum = 3, Parking = False, Rented = False, Price = 1000)
Instance 2 : (RoomsNum = 5, Parking = True, Rented = True, Price = 2000)
Instance 3 : (RoomsNum = 3, Parking = True, Rented = False, Price = 1200)
Instance 4 : (RoomsNum = 2, Parking = False, Rented = True, Price = 800)
Instance 5 : (RoomsNum = 4, Parking = True, Rented = False, Price = 1700)
Instance 6 : (RoomsNum = 3, Parking = False, Rented = False, Price = 1000)
Instance 7 : (RoomsNum = 4, Parking = False, Rented = True, Price = 1500(

'''

apartment_1 = Apartment(ro = 3, pa = False, re = False, pr = 1000)
apartment_2 = Apartment(ro = 5, pa = True,  re=  True,  pr= 2000)
apartment_3 = Apartment(ro = 3, pa = True,  re=  False, pr = 1200)
apartment_4 = Apartment(ro = 2, pa = False, re = True,  pr = 800)
apartment_5 = Apartment(ro = 4, pa = True,  re=  False, pr = 1700)
apartment_6 = Apartment(ro = 3, pa = False, re = False, pr = 1000)
apartment_7 = Apartment(ro = 4, pa = False, re = True,  pr = 1500)



'''
Exercise 3:
With the same python file you have created in Exercise 2, create an empty list and add 
all the previous instances to this list.
'''

all_instances = [apartment_1, apartment_2, apartment_3, apartment_4, apartment_5, apartment_6, apartment_7]


'''
Exercise 4:
Write the following functions in the same python file you have created in Exercise 2:
A) num_Available(self, list): that accepts a list of apartments and returns how 
   many apartments are available (not rented). 
Testing:If I call this method with the list you created in Exercise 3, the output should be 4 as 
there are 4 apartments which are not rented yet. 
'''


def num_available(my_list):
    for inst in my_list:
        if not inst['re']:
            return inst


num_available(all_instances)

'''
B) num_Apartment_Rooms(self, list, rNum): that accepts a list of apartments, 
rNum (int), and returns how many apartments that have this number of rooms. 
Testing:
If I call this method with the list you created in Exercise 3 and rNum=4, the output 
should be 2 as there are 2 apartments which have 4 rooms.
C) apartment_Search(self, list, park, price): that accepts a list of apartments, park
(boolean), price (int), and print out the info for all apartments that meets the 
parking condition and has a rental price less than the specified price. '''

