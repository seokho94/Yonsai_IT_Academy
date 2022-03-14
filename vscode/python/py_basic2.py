from random import *


a = [1,2,3,['a','b','c']]
print(a)
print(a[0])
print(a[-1][0])
print(a[3][0])

print(len(a))
print(len(a[3]))

b = [1 for i in range(5)]

print(b)
print(len(b))

print(b*2)

print(a+b)

del a[-1][2]

print(a)

a[-1].append('c')

print(a)

c = [0 for i in range(6)]

for i in range(len(c)) :
    c[i] = randint(1,9)
    
print(c)

def bubble(arr) :
    index = 0
    lastIndex  = len(arr)
    while True :
        if(arr[index] > arr[index+1]) :
            temp = arr[index+1]
            arr[index+1] = arr[index]
            arr[index] = temp
        else :
            index+=1
            if(index+1==lastIndex) :
                index = 0
                lastIndex -=1
                if(lastIndex==2) : break
                
bubble(c)

print(c)
