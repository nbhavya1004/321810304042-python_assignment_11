#   321810304042-python_assignment_11

#   Bhavyasree N - 321810304042


#     1.     Write a python program to sum all the  elements in a list.

# METHOD_1 :

list=[ ]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    list.append(numbers)
print("Sum of elements in given list is :",sum(list))


# METHOD_2 :

sum = 0
list = [5,6,7,72,89]
for ele in list: 
    sum = sum+ ele
print("Sum of all elements in given list: ", sum) 


   
#     2.     Write a python program to multiply all elements in a list.

# METHOD_1 :

import numpy
list=[ ]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    list.append(numbers)
print("Product of elements in given list is :",numpy.prod(list))


# METHOD_2 :

product=1
list=[3,5,4,6]
for i in list:
	product=product*i
print("multiplication of items in a list:",product)



#     3.     Write a python program to get the largest(max) and smallest(min) numbers from list.

# METHOD_1 :

list=[ ]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    list.append(numbers)
print("Maximum element in the list is :",max(list),"\nMinimum element in the list is :",min(list))


# METHOD_2 :

list=[34,5,6,12,78]
a=max(list)
b=min(list)
print("max number in a list:",a)
print("min number in a list:",b)



#     4.     Write a python program to remove duplicates from list.

# METHOD_1 :
	
a=[ ]
num=int(input('How many numbers: ')) 
for n in range(num):
    numbers=int(input('Enter number: '))
    a.append(numbers)
b=set()
unique=[]
for n in a:
    if n not in b:
        unique.append(n)
        b.add(n)
print("Non-duplicate items:")
print(unique)


# METHOD_2 :

a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)



#     5.     Write a python program to check list is empty or not.

# METHOD_1 :

a=[ ]
if len(a) == 0:
    print("The list is empty")


# METHOD_2 :

list=input("enter elements of a list:")
for i in list:
	if i==0:
		print("list is empty")
	else:
		print("list is not empty")



#     6.     Write a python program to clone or copy a list.

# METHOD_1 :

list1=[1,2,3]
list2=list1[:]
print("Before cloning:",list1)
print("After cloning:",list2)


# METHOD_2 : 

oldlist=[1,2,3,4,5]
newlist=oldlist
print("oldlist:",oldlist)
print("newlist:",newlist)



#     7.     Write a python program to print specified list after removing 0th and 4th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4)]
print(color)



#     8.     Write a python program to remove elments in even.

# METHOD_1 :
	
num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)
	

# METHOD_2 :

list = [4,5,6,7,8,1,2,3]
print("Original list:",list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print ("list after removing EVEN numbers:",list)



#     9.     Write a python program to shuffle and print specified list:

# METHOD_1 :

from random import shuffle
color=['Red','Green','White','Black','Pink','Yellow']
shuffle(color)
print(color)


# METHOD_2 :

import random 
list= [1, 4, 5, 6, 3]
print ("The original list is : ",list) 
random.shuffle(list) 
print ("The shuffled list is : " ,list) 



#     10.     Write a python program to get the difference between two elements in a list.

# METHOD_1 :
	
a=[1,2,3,4,5]
d=[4,5]
print(set(a)-set(d))


# METHOD_2 :

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 70]
print ("List1:", list1)
print("List2:", list2)
print("Difference elements:")
print ((set(list1) - set (list2)) )