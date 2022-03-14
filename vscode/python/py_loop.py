#반복문 for, while, do-while
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