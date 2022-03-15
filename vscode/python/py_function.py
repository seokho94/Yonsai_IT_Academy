#Python function 사용
#매개변수 지정시 위치가 바뀌어도 정상 작동
def add(a, b) :
    return a*2+b*4
result = add(b=2,a=3)
print(result)

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
        
say_myself('갤럭시', 21)
say_myself('아이폰', 12, False)

numPlusnum = lambda a, b : a+b
result = numPlusnum(3,4)
print(result)