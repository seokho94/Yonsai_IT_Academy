#실수형 float 알아보기

성적0 = float(input('0번 학생의 성적을 입력해주세요'))
성적1 = float(input('1번 학생의 성적을 입력해주세요'))
성적2 = float(input('2번 학생의 성적을 입력해주세요'))
성적3 = float(input('3번 학생의 성적을 입력해주세요'))
성적4 = float(input('4번 학생의 성적을 입력해주세요'))

print('--- 입력된 값 ---')
print('0번 학생의 성적: {}' .format(성적0))
print('1번 학생의 성적: {}' .format(성적1))
print('2번 학생의 성적: {}' .format(성적2))
print('3번 학생의 성적: {}' .format(성적3))
print('4번 학생의 성적: {}' .format(성적4))

#위에 작성된 코드 간편화하기

성적 = [0.0] * 5

for 번호 in range(5) :
    성적[번호] = float(input('{}번 학생의 성적을 입력하세요:'.format(번호)))

print('=== 입력된 값 ===')

for 번호 in range(5) :
    print('{}번 학생의 성적: {}'.format(번호, 성적[번호]))