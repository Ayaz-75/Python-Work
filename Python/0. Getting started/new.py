




'''my_dic={'Name':'Ayaz','Age':21}
print('Name is: ',my_dic['Name'])
print('Age is: ',my_dic['Age'])
'''

#t=(1,2,3,4)
#print(t.index(4))


'''myset=set()

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)'''

#print(100**0.5)
#print(25**0.5)



'''hungry=False
if hungry:
    print('Feed me.!')
else:
    print("I'm not hungry ")

'''
'''
a=5
b=2
c=3
print(a+(b==2))'''



'''
x=4
y=3
z=2
a=x+y>x/z
print(type(a))'''

'''a=True
b=5
c=2.0
x=a+b//c
y=b%c>=1 and a
print(x)
print(type(x))
print(y)
print(type(y))

'''
'''a=12
print(a)
print(type(a))
b='good day'
print(b)
print(type(b))
'''
'''
x='hello'
x='goodbye'
print('hello',x)


x=90
z='hello'
print(x,z)'''


'''
avalue = 3.14
bvalue = 35
if not(avalue <= 20) or (bvalue < 20):
    print('Thank you')
print('Did the code within the if statement execute?')
'''
'''
avalue = 20
bvalue = 15
if (avalue > 20) and (bvalue < 20):
    print('Thank you')
else:
    print('You are welcome')
print('You are here')


'''
'''
avalue = -22.5
bvalue = 2.1
if avalue>1:
    print('Code group 1 executes')
elif not(avalue>1 and bvalue>4):
    print('Code group 2 executes')
else:
    print('Code group 3 executes')
    print('Which code group executed?')

'''
'''
flag=0
while flag==0:
    z=float(input('Enter a number between 0 and 10: '))
    print()
    if z>=0 and z<=10:
        flag=1
    else:
        print('Input error -- please try again')
        print()
print('Explain what the while loop is doing.')'''
'''

for i in range(0,5):
    for j in range(0,4):
        print('i =',i,' j=',j, ' i*j=',i*j)

'''
'''
aval=4
for i in range(9,0,-1):
    print('i = ', i)
    if i < aval:
        print('stopping here ...')
        break
print('Program terminating')'''
'''
aval=4
for i in range(9,0,-1):
    if i == aval:
        continue
    print('i=',i)

'''

'''
aval=4
for i in range(9,0,-1):
    if i == aval:
        pass
        print('What does the pass instruction do?')
    print('i=',i)
'''

'''
no=float(input('Input a number: '))
if no>-5 and no<=0:
    print(no*2)
elif no>0 and no<=3:
    print(no*3)
elif no>3 and no<=7:
    print(no*4)
else:
    print(no/10)
'''
'''
no=int(input('Input an integer between 1 and 5: '))
if no>0 and no<=10:
    for no in range(1,no+1):
        print(no)
else:
    print('You did not enter a value between 1 and 5 ')


'''

'''

i=int(input('Enter no: '))
for i in range(1,i):
    print(i)

'''

'''

'''
'''
num=int(input('Input an integer greater than 5 and less than or equal to 10: '))
if num>5 and num<=10:
    for i in range(0,num+1):
        print(i)
        if i*10>=70:
            break

else:
    print('You did not enter a value between 5 and 20')
'''


'''
num=int(input('Input a number greater than zero and less than or equal to 10: '))
if num>5 and num<=10:
    for i in range(5,10):
        print()
else:
    print('You did not enter a value between 0 and 10')

'''

'''
a=3
b=2
c=a**b
print(c)
'''
'''
a=3
b=4
c=[a, b]
d=[c, a]
e=d+d
print(e[2])'''

'''x=[ ]
for i in range(3):
    x.append(i)
    x.extend(x)
print(x)'''


'''xvals=['there', 'everywhere', 'herehere', 'zero', 'nowhere']
y=[ ]
for x in xvals:
    y.append(x.find('ere'))
print(y)
'''


'''x=[2, 3, 4, 5, 'a', 'bee', 'c', 'dee']

print(x[:])	

print(x[1:3])	

print(x[1:8:2])	

print(x[3:1:-1])

print(x[2:len(x)])	

print(x[2:])	

print(x[:3])	

print(x[-4:-1])	

print(x[-1])	

print(x[::2])'''






'''x=[1, 2, 3, 4, 5, 6, 7, 8]
y=x[::2]
z=y.copy()
y.append(x[1::2])

z.extend(x[1::2])
print(y)
print(z)'''

'''x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=x[-1:-5:-1]
z=x[::3]
for i in range(len(z)):
    print(y[i],z[i])'''


a=[1,2,3,4,5,6,7,8,9,10]
'''for i in a:
    if i%2==0:
        print('Ayaz',i)
    else:
        print(f'Odd number: {i}')'''
a_sum=0
for i in a:
    a_sum+=i
    #print(a_sum)
print(a_sum)