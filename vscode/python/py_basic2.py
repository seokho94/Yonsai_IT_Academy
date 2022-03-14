from random import *

#list
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

print(c.pop())
print(c.count(1))

#tupple
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t2[0])
print(t2+t3)
print(t4[0:1])
print(len(t5))

#dictionary
a = {1: 'a'}
a[2] = 'b'
print(a)

del a[1] #1은 index 값이 아닌 key 값
print(a)

grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey'])
print(grade['julliet'])

b = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1118'}
print(b.keys())

for k in b.keys() :
    print(k)
    
print(b.values())

for k in b.values() :
    print(k)
    
print(b.items())

for i in b.items() :
    print(i)

print('name' in b)
print(b.get('none'))
print(b.get('name'))
print(b.get('none', '111')) #none이 없다면 phone 출력
print(b.get('name', 'phone'))
    
b.clear()
print(b)

#set
s2 = set("Hello")
l1 = list(s2)
l2 = list(set('HelloWorld'))
print(s2)
print(l1[0])
print(l2)

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s3&s4)
print(s3.intersection(s4))
print(s3|s4)
print(s3.union(s4))
print(s3-s4)
print(s3.difference(s4))
print(s3)
s5 = s3&s4
s6 = s3|s4
print(s3|s4-s5)
print(s6-s5)
s3.add(7)
print(s3)
s3.update([9,10,11])
print(s3)
s3.remove(9)
print(s3)

#bool
a = True
print(type(a))
print(1==1)
print(1<2)
print(1>2)
print(bool(""))
print(bool("1"))
print(bool())
print(bool([]))
print(bool([1,2,3]))