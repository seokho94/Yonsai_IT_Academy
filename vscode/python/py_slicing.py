#1번
점수A = [60, '결석', 60, 70]
점수B = 점수A

print(점수B[2])

점수A[2] = 100
print(점수B[2]) #100 출력

#id = 주소를 참조 / reference 개념
print(id(점수A))
print(id(점수B))

#1번 코드를 slicing

점수A = [60, '결석', 60, 70]
점수B = 점수A[:]

print(점수B[2])

점수A[2] = 100
print(점수B[2]) #60 출력

print(id(점수A)) #주소 : 2032256969472
print(id(점수B)) #주소 : 2032257232128

'''
점수B[2] 값이 다른 이유는?
=>점수B = 점수A[:]  : 값을 전체를 복사하여서 값을 입력
=>점수B = 점수A : 점수A라는 배열을 점수 B에 입력
'''