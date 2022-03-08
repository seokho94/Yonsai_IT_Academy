#method 생성하기

class 참치선물세트() :
    일반 = 0
    야채 = 0
    고추 = 0

    #총합 method
    def 총합(self, 이름) :
        합 = self.일반 + self.야채 + self.고추
        return 이름 + str(합)
    
    #출력 method
    def 출력(slef, 이름) :
        print('**', 이름, '**')
        print('일반참치', slef.일반)
        print('야채참치', slef.야채)
        print('고추참치', slef.고추)

참01호 = 참치선물세트()
참01호.일반 = 12
참01호.야채 = 3
참01호.고추 = 3

출력값 = 참01호.총합('참치선물세트 01호 내용물 : ') #method 호출

print(출력값+'\n')

참01호.출력('참치선물세트 01호 내용물')