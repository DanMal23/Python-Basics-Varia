#!/usr/bin/env python
# coding: utf-8

# 3-dim list
a = [[[1,2],[3,4],5], [6,7]]
a[0][0][1] #2
a[0][1][0] #3
a[0][2] #5
a[1][0] #6
a[1][1] #7


b= [[1,2],3]
b*=3 # a 'copy'
print(b)
# [[1, 2], 3, [1, 2], 3, [1, 2], 3]
len(b) #6 - list counts as 1 elem
b[1] = '3a'
b[3] = '3b'
b[5] = '3c'  #  [[1, 2], '3a', [1, 2], '3b', [1, 2], '3c']
b[2][0]='1a'
b[0][1]='$'  # [['1a', '$'], '3a', ['1a', '$'], '3b', ['1a', '$'], '3c']
b[0][0]= 0
print(b)


numb=3
th=['sth', 0, [1,2,numb], 4,4.5]
th[1] #0
th[2] # [1, 2, 3]
th[2][2] #3
th[3] #4
th.insert(5,6) # at position index_5 insert numb 6
# ['sth', 0, [1, 2, 3], 4, 4.5, 6]
th.index(4.5) # at index 4
th.index([1,2,numb]) #2
#th.sort() #'<' not supported between instances of 'int' and 'str'


# 2-dim list
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
c[0][0] = 5
c[1][0] = 6
c[2][0] = 7
c # [[5,0,0],[6,0,0],[7,0,0]]


e = [[0,0,0]]
e*=3 # copies
e[0][0]=4 # same nums because it's a 'copy'
e # [[4,0,0],[4,0,0],[4,0,0]]


def d1(row,col):
    return [['*' for x in range(col)] for y in range(row)]
g = d1(3,4)
g[0][0]=0
g[1][1]=1
g[2][2]=2
g  # [['0','*','*','*'],['*','1','*','*'],['*','*','2','*']]


def dl2(row,col):
    return [['*' for x in range (col)] for y in range(row)]
h = dl2(2,4)
# x- row number/content; y - column numb ?
h[0][0]=0
h[0][2]=2
h[1][1]=1
h[1][3]=3  #  [[0, '*', 2, '*'], ['*', 1, '*', 3]]
h[1].reverse()  # [[0, '*', 2, '*'], [3, '*', 1, '*']]
h[0].pop(0) # [['*', 2, '*'], [3, '*', 1, '*']]
h[0].remove('*') # [[2, '*'], [3, '*', 1, '*']]
h[0].extend([1,'$']) # [[2, '*', 1, '$'], [3, '*', 1, '*']]
h[0].clear() # [[], [3, '*', 1, '*']]
h[1].remove('*')
h[0].append(8) # [[8], [3, 1, '*']]
h[0].insert(0,6) # inserts 6 at index 0 in the 1st list
h #[[6, 8], [3, 1, '*']]

