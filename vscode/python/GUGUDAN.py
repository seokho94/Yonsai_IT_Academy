def GUGU(n) :
    arr = [0 for i in range(9)]
    for i in range(len(arr)) :
        arr[i] = n*(i+1)
    return arr

def GUGU_2(n) :
    arr = []
    for i in range(9) :
        arr.append(n*(i+1))
    return arr
    
result = GUGU(2)
result2 = GUGU_2(2)

print(result)
print(result)