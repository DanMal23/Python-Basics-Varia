#!/usr/bin/env python
# coding: utf-8

# tuples
tuple1 = (1,2,3,4,5,6,)
print(tuple1[:-2]) # (1, 2, 3, 4)
print(tuple1[-2:]) # (5, 6)
print(tuple1[-1:]) # (6,)
print(tuple1[:-1]) # (1, 2, 3, 4, 5)
#reversed order of elements in the output:
print(tuple1[::-1]) # (6, 5, 4, 3, 2, 1)

tup2=(0,1,2,3,4,5,6,7,8,9,10)
print(tup2[::-2])  # (10, 8, 6, 4, 2, 0)
print(tup2[::2]) # (0, 2, 4, 6, 8, 10)
print(tup2[1::2]) # (1, 3, 5, 7, 9)
print(tup2[4::2]) # (4, 6, 8, 10)
print(tup2[4::-1]) # (4, 3, 2, 1, 0)


# 'tuple' object does not support item assignment
# but you can modify internal list
tuple2 = (1,2,3,[4,5,6], [7,8])
tuple2[3][0]='*'  
print(tuple2)   #(1, 2, 3, ['*', 5, 6], [7, 8])
tuple2[4][0]=0  
print(tuple2)  #(1, 2, 3, ['*', 5, 6], [0, 8])
tuple2[3][1]='$'   #index 1; 3rd element
print(tuple2) # (1, 2, 3, ['*', '$', 6], [0, 8])
print("length of tuple:",len(tuple2)) # list counts as 1 
# length of tuple: 5


x=[1,2,3]
y=[4,5,6]
tuple3=(x,y)
z=[7,8,9]
tuple3=(x,y,z) # ([1, 2, 3], [4, 5, 6], [7, 8, 9])
tuple3[0][1]=0 #1st row, second colum
tuple3[2].append(0) # ([1, 0, 3], [4, 5, 6], [7, 8, 9, 0])
tuple3[1].append('$') #adds to the end of second list which has index1
tuple3 # ([1, 0, 3], [4, 5, 6, '$'], [7, 8, 9, 0])


t = ('a',1, 2.0, [3,4,5,6], [7,8,9, [7,9]])
t[4][3][0]='$'
# ('a', 1, 2.0, [3, 4, 5, 6], [7, 8, 9, ['$', 9]])
t[4][3].append('*')
t  # ('a', 1, 2.0, [3, 4, 5, 6], [7, 8, 9, ['$', 9, '*']])

