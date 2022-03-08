인사 = '안녕하세요'

#in 키워드를 사용한 조건문
if '녕' in 인사 :
    print('있어요')

else:
    print('없어요')

print('\n')

#in 키워드를 사용한 반복문
'''
Java에서 배열 출력 방식과 비슷
arr = [1,2,3,4,5]
for(int i : arr) println(i);
'''
for 단어하나 in 인사:
    print(단어하나)

print('\n')

#in키워드를 사용하여 공백 글자 수 세기
문장 = input('아무 글이나 입력하세요:')
글자수 = 0

for 한글자 in 문장:
    if 한글자 != ' ' :
        글자수 +=1

print(문장*글자수)