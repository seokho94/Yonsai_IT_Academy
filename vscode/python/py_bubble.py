from random import randint


arr = [0 for i in range(5)]

for i in range(len(arr)) :
    arr[i] = randint(1,9)

def bubble(arr) :
    index = 0
    lastIndex = len(arr)
    while True :
        if(arr[index]>arr[index+1]) :
            arr[index],arr[index+1] = arr[index+1],arr[index]
        else :
            index+=1
            if(index+1==lastIndex) :
                index=0
                lastIndex-=1
                if(lastIndex==2) :
                    break
                
print(arr)
bubble(arr)
print(arr)