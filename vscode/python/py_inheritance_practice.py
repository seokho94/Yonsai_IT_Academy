class 세면도구 : 
    def __init__(self, 치약, 샴푸, 비누) :
        self.치약 = 치약
        self.샴푸 = 샴푸
        self.비누 = 비누

    def 내용물출력(self, 세트이름) :
        print(세트이름)
        print('치약 : ', self.치약)
        print('샴푸 : ', self.샴푸)
        print('비누 : ', self.비누)

class 특별세트(세면도구) :

    def __init__(self, 치약, 샴푸, 비누, 면도기):
        super().__init__(치약, 샴푸, 비누)
        self.면도기 = 면도기

    def 내용물출력(self, 세트이름) :
        super().내용물출력(세트이름)
        print('면도기 : ', self.면도기)

특01호 = 특별세트(1, 2, 3, 1)
특01호.내용물출력('명절 특별세트 01호')