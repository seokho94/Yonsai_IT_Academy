food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

multiline = '''
Life is too short
You need python
'''

multiline2 = """
Life is too short
You need python
"""

print(multiline)
print(multiline2)

print("%20sjane" % 'test')
print("%-20sjane" % 'test')

print("%f" % 3.141592)
print("%0.5f" % 3.141592)
print("%0.4f" % 3.141592)
print("%10.4f" % 3.141592)

#arr.count('b') 배열에서 b의 개수 출력
a= "hobby"
print('a문자열에서 b의 개수 : %d' %a.count('b'))

#arr.find('a')  배열에서 a의 최초 인덱스 출력, 없다면 -1 출력 
a = "Python is the best choice"
print('a문자열에서 k의 최초 인덱스 : %d' %a.find('k'))

#arr.index('a') find와 같지만 a가 없다면 오류 발생
a = "Python is the best choice"
print('a문자열에서 i의 최초 인덱스 : %d' %a.index('i'))

#arr.join() 문자열 삽입
a = ""
print('a에 문자열 삽입 전 : ', a,'\na에 문자열 삽입 후 : ', a.join('abcd'))

#arr.upper() 문자열 대문자 변환
a = 'abcd'
print('a에 문자열 대문자 변환 전 : ', a,'\na에 문자열 대문자 변환 후 : ', a.upper())

#arr.lower() 문자열 대문자 변환
a = 'ABCD'
print('a에 문자열 소문자 변환 전 : ', a,'\na에 문자열 소문자 변환 후 : ', a.lower())

#가장 왼쪽 연속 공백 삭제 arr.lstrip()
a = '         a bcd'
print('a에 문자열 왼쪽 공백 제거 전 :', a,'\na에 문자열 왼쪽 공백 제거 후 :', a.lstrip())

#가장 오른쪽 연속 공백 삭제 arr.rstrip()
a = 'abcd           '
print('a에 문자열 오른쪽 공백 제거 전 :', a,'\na에 문자열 오른쪽 공백 제거 후 :', a.rstrip())

#양쪽 연속 공백 삭제 arr.strip()
a = '         abcd       '
print('a에 문자열 양쪽 공백 제거 전 :', a,'\na에 문자열 양쪽 공백 제거 후 :', a.strip())

#문자열 변경 arr.replace('a','b'), a를 b로 변경
a = 'Life is too short'
print('a에 문자열 수정 전 :', a,'\na에 문자열 수정 후 :', a.replace("Life", "Your Leg"))

#문자열 변경 arr.split(), 소괄호 안에 입력한 값을 기준으로 나눔 if null이라면 공백
a = 'Life is too short'
b = "a:b:c:d"
print('a에 문자열 분리 전 :', a,'\na에 문자열 분리 후 :', a.split())
print('b에 문자열 분리 전 :', b,'\nb에 문자열 분리 후 :', b.split(':'))