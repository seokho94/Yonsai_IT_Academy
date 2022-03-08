from msilib.schema import SelfReg


class 참치선물세트() :
    def __init__(self, 일반, 야채, 고추) :
        self.일반 = 일반
        self.야채 = 야채
        self.고추 = 고추

    def 출력(self, 이름) :
        print('**', 이름, '**')
        print('일반참치 : ', self.일반)
        print('야채참치 : ', self.야채)
        print('고추참치 : ', self.고추)


class 특별세트(참치선물세트) :

    def __init__(self, 일반, 햄, 카놀라유) :
        super().__init__(일반, 0, 0)
        self.햄 = 햄
        self.카놀라유 = 카놀라유

    def 출력(self, 이름):
        super().출력(이름)
        print('햄 : ', self.햄)
        print('카놀라유 : ', self.카놀라유)


특01 = 특별세트(6,3,2)
특01.출력('특별세트 01호')