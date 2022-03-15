#반복문 for, while, do-while

#while문
treehit = 0
while treehit < 10 :
    treehit+=1
    print("나무를 {}번 찍었습니다.".format(treehit))
    if(treehit==10) :
        print("나무가 넘어갑니다.")
        
coffee = 10
money = 300
while money :
    print("커피가 나왔습니다.")
    coffee -=1
    print("남은 커피의 양은 %d" %coffee)
    if coffee == 0 :
        print("남은 커피가 없습니다.")
        break
print("판매를 중지합니다.")

a=0
while a<10 :
    a = a+1
    if a%2 ==0 : continue
    print(a)
    
#for문  문법 : for i in range(a,b,1) -> a부터 b까지 1씩 증가
#list, tuple, String 바로 출력 : for i in list or tuple or string
#->Java에서 for i : arr 과 동일한 기능
test_list = ['one','two','three']
for i in test_list :
    print(i)

#구구단
print("구구단")
for i in range(2,10,1) :
    for j in range(1,10,1) :
        print("{} X {} = {}".format(i,j,i*j))

#List 내포 사용법
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)

result2 = [num*3 for num in a]
print(result2)

result3 = [num*3 for num in a if num % 2 == 0]
print(result3)

result4 = [x*y for x in range(2,10) for y in range(1,10)]
print(result4)