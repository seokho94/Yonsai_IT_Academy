#구구단 n단 리스트 크기 선언하고 값 입력 후 반환
def GUGU(n) :
    arr = [0 for i in range(9)]
    for i in range(len(arr)) :
        arr[i] = n*(i+1)
    return arr

#구구단 n단 가변 리스트에 append로 값 입력 후 반환
def GUGU_2(n) :
    arr = []
    for i in range(9) :
        arr.append(n*(i+1))
    return arr
    
result = GUGU(2)
result2 = GUGU_2(2)

print(result)
print(result)