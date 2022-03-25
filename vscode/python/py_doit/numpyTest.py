import scipy as sp
import numpy as np
import pandas as pd

discount = .05
cashflow = 100

def presentvalue(n) :
    return (cashflow / ((1 + discount)**n))

print(presentvalue(1))
print(presentvalue(2))

for i in range(20) :
    print(presentvalue(i))
    
loss = [-750, -250]
profit = [100] * 18
print(profit)

a = np.array([[2,3],[5,2]])
print(a)

d = np.array([2,3,4,5,6])
print(d)
print(d.shape)

e = np.array([[1,2,3,4], [3,4,5,6]])
print(e)
print(e.shape)

data = np.arange(1,5)
print(data.dtype)

print(data.astype('float64'))
print(data.astype('int32'))

z = np.zeros((2,10))
print(z)

o =  np.ones((2,10))
print(o)

r = np.arange(2,14)
print(r)

c = np.ones((2,3))
print(c)
b = np.transpose(c)
print(b)

arr1 = np.array([[2,3,4],[6,7,8]])
arr2 = np.array([[12,23,14],[36,47,58]])

arr3 = arr1 + arr2
print(arr3)

arr4 = arr1 * arr2
print(arr4)

arr5 = arr1 / arr2
print(arr5)

arr6 = np.array([100,200,300])
a1 = arr1.shape
a6 = arr6.shape

a7 = a1 + a6
print(a7)
arr7 = arr1 + arr6
print(arr7)

arr8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr8.shape
arr1.shape

arr10 = np.array([[9],[3]])
arr10.shape
print(arr1)
print(arr10+arr1)

d = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,7,8,9,9]])
d_list = [[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]]
d[:2] = 0
print(d)