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

#enumerate(X)
#->순서가 있는 자료형을 입력 받아 인덱스 값을 포함하는 enumerate 객체 반환
for i, name in enumerate(['body','foo','bar']) :
    print(i,name)
print()

#eval(expression)
#-> 문자열을 실행한 결과값을 반환
#-> 숫자 연산이 가능한 경우 숫자연산, 불가능한경우 문자열 연산
print(eval('2+2'))
print(eval("'hi' + 'roo'"))
print(eval("'1'+'hi'"))

#filter(fuction, iterable) iterable 자료형의 요소가 fuction에 입력되었을 때 반환 값이 참인 것만 반환
def positive(X) :
    return X > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 8])))

#hex(X)->16진수 변환
print(hex(23))

#id(X) X의 고유 주소 값 반환
ada = 1011
print(id(ada))

#input([prompt]) 사용자 입력 값을 받아오는 함수
a = input()
b = input("Enter: ")

#int(X) X를 정수형으로 변환
print(int(3.14159))

#int(x,radix) raix 진수 문자열을 10진수로 변환
print(int('1A', 16))

#instance(object, class) object가 class의 인스턴스인지 판단하여 bool 값 반환
class Person: pass

a = Person()
print(isinstance(a,Person))
b=3
print(isinstance(b,Person))

#len(X) -> 문자열이나 자료형의 길이 값 출력
print(len("python"))

#list(iterable) -> 자료형을 리스트로 변환
print(list("python"))

#map(fuction, iterable) -> iterable 자료형을 각요로를 fuction이 수행한 결과를 묶어서 반환
def two_times(X) : return X*2
print(list(map(two_times,[1,2,3,4])))

#max(iterable) -> iterable 자료형의 최댓값 반환
print(max([1,2,3]))
print(max("python"))

#min(iterable) -> iterable 자료형의 최솟값 반환
print(min([1,2,3]))
print(min("python"))

#oct(X) -> X를 8진수 문자열로 반환
print(oct(34))

#ord(c) -> 문자이ㅡ 아스키 코드 값 반환
print(ord('a'))

#pow(x,y) x의 y 제곱 값 반환
print(pow(2,2))

#range([start],stop,[step]) -> []생략가능 , 입력받은 숫자에 해당 범위 값을 객체로 반환
print(list(range(5)))

#round(number, [ndigits]) -> []생략가능, 반올림
print(round(4.6))
print(round(5.678, 2))

#sorted(iterable) -> 입력 값을 정렬한 후 리스트로 반환
print(sorted([3,1,2]))
print(sorted(['a','b','d','a']))

#str(object) -> object를 문자열 형태로 변환
print(str(3))

#sum(iterable) -> 리스트나 튜플의 모든 요소의 합 반환
print(sum([1,2,3]))

#tuple(iterable)
print(tuple("abn"))

#type(object) -> object의 자료형 반환
print(type("avb"))
print(type(123))

#zip(*iterable) -> 동일 개수로 이루어진 자료형을 묶어주는 역할 / 같은 인덱스끼리 묶음
print(list(zip([1,2,3],[4,5,6],[7,8,9])))