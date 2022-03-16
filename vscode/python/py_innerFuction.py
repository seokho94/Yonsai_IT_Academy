#abs(X) -> X의 절댓값 반환
print(abs(-3))

#all(X) -> 요소가 반복적인지 확인 
# -> 반복가능한 자료형 X가 모두 참이면 True, 하나라도 거짓이면 False (And연산)
print(all([1,2,3,0]))

#any(X) -> 같은 자료형인지 확인 
# -> X가 모두 거짓이면 false , 하나라도 참이면 True (OR연산)
print(any([1,2,3,"A"]))

#chr(X)
#->아스키 코드(X)를 문자로 반환
print(chr(97))

#dir(X) -> 객체 자체 변수나 함수를 반환
print(dir([1,2,3]))

#divmod(a,b)
#->a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
c = divmod(4,3)
print(c)

#enumerate(X)
#->순서가 있는 자료형을 입력 받아 인덱스 값을 포함하는 enumerate 객체 반환
for i, name in enumerate(['body','foo','bar']) :
    print(i,name)
    
#eval(expression)
#-> 문자열을 실행한 결과값을 반환
print(eval('1+2'))
print(eval("'hi' + 'roo'"))
print(eval("'1'+'hi'"))
