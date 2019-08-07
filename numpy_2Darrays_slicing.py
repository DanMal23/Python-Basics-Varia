# creating a 2D array: 4 rows, 4 columns;
# numbers in order from 0-15 for all array

import numpy as np
x = [[(i+j*4) for i in range(4)] for j in range(4)]
arr = np.asarray(x) # or np.array(x)
print(arr)
'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]'''
 
 arr.reshape(16)[::5] 
 '''array([ 0,  5, 10, 15])'''
 # output: elems on the diagonal; every 5th elem starting from 0
 
 arr[0:4,::-4]
 '''[[ 3]
 [ 7]
 [11]
 [15]]'''
 # all rows from every 4th col, starting from 4th as cols are reversed (::-)
 
arr[::4] 
'''[[0 1 2 3]]'''
# 1st row (index [0])and then every 4th if exists

arr[:,::4]
'''[[ 0]
 [ 4]
 [ 8]'''
 # all rows from every 4th col starting from 1st (index [0])
 
 arr[:,::2] 
 '''[[ 0  2]
 [ 4  6]
 [ 8 10]'''
 # all rows from every 2nd col starting from 1st (index [0])

arr[1:,::2]
'''[[ 4  6]
 [ 8 10]
 [12 14]]'''
 # rows from index [1], cols from index [0] - every 2nd
 
arr[:,1::2]
'''[[ 1  3]
 [ 5  7]
 [ 9 11]
 [13 15]]'''
 # all rows, col starts from [1] every 2nd
 
 arr[2:,2::2]
'''[[10]
 [14]]'''
 # row from index[2], cols from index [2] every 2nd 

arr[3,::-2] 
''' [[15 13]] '''
 # rows at index [3], cols reversed every 2nd
