from time import sleep


class TunaCanSet():
    def __init__(self, normal, veg, pepper) :
        self.normal = normal
        self.veg = veg
        self.pepper = pepper

    def content_show(self, name) :
        print('****', name , '****')
        print('Normal Tuna : ', self.normal)
        print('Vegitable Tuna : ', self.veg)
        print('Pepper Tuna : ', self.pepper)

tuna01 = TunaCanSet(12, 5, 6)
tuna01.content_show('Tuna GiftSet 01')
print()


class 세면도구:
    def __init__(self, 치약, 샴푸, 비누) :
        self.치약 = 치약
        self.샴푸 = 샴푸
        self.비누 = 비누

    def 내용물출력(self, 세트이름) :
        print(세트이름)
        print('치약 : ', self.치약)
        print('샴푸 : ', self.샴푸)
        print('비누 : ', self.비누)

세01호 = 세면도구(1, 2, 3)
세02호 = 세면도구(4, 2, 2)

세01호.내용물출력('세면도구세트 01호 내용물')
세02호.내용물출력('세면도구세트 02호 내용물')