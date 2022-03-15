#클래스 개념

#세면도구 클래스 생성
class 세면도구 :
    치약 = 0
    샴푸 = 0
    비누 = 0

#세01호 인스턴스 생성
세01호 = 세면도구()
세01호.치약 = 1
세01호.샴푸 = 2
세01호.비누 = 3

#세02호 인스턴스 생성
세02호 = 세면도구()
세02호.치약 = 4
세02호.샴푸 - 2
세02호.비누 = 2

print('세면도구 01호의 내용물')
print('치약 : ', 세01호.치약, ' 샴푸 : ', 세01호.샴푸, ' 비누 : ', 세01호.비누)

print('세면도구 02호의 내용물')
print('치약 : ', 세02호.치약, ' 샴푸 : ', 세02호.샴푸, ' 비누 : ', 세02호.비누)

class FourCal : 
    def __init__(self, first, second) :
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def sub(self) : 
        result = self.first - self.second
        return result
    def mul(self) : 
        result = self.first * self.second
        return result
    def div(self) : 
        result = self.first / self.second
        return result   
        
a = FourCal(4,2)
b = FourCal(5,3)
print("a.first : {}, a.second : {}, a.first + a.second = {}".format(a.first, a.second, a.add()))
print("b.first : {}, b.second : {}, b.first + b.second = {}".format(b.first, b.second, b.add()))
print("a.first - a.second = {}".format(a.sub()))
print("b.first - b.second = {}".format(b.sub()))
print("a.first * a.second = {}".format(a.mul()))
print("b.first * b.second = {}".format(b.mul()))
print("a.first / a.second = {}".format(int(a.div())))
print("b.first / b.second = {}".format(int(b.div())))

#클래스 상속
class MoreFouCal(FourCal) :
    pass

c = MoreFouCal(4,2)
print("c.first + c.second = {}".format(c.add()))
print("c.first - c.second = {}".format(c.sub()))
print("c.first * c.second = {}".format(c.mul()))
print("c.first / c.second = {}".format(int(c.div())))

class Family :
    lastname = "김"
    
print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname ="박"
print(a.lastname)
print(b.lastname)
if(id(Family.lastname)==id(a.lastname)) :
    if(id(a.lastname)==id(b.lastname)) :
        print("Family.lastname == a.lastname == b.lastname")
else :
    print("3개의 주소값이 다릅니다.")