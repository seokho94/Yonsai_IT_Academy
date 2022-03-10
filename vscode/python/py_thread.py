import threading

class 숫자세기 :

    def __init__(self, 나의이름) :
        self.나의이름 = 나의이름

    def 셈하기(self):
        for 숫자 in range(0, 5):
            print(self.나의이름, 숫자)

첫번째 = 숫자세기('첫번째')
두번째 = 숫자세기('두번째')

첫번째.셈하기()
두번째.셈하기()

class 스레딩숫자세기(threading.Thread) :
    def __init__(self, 나의이름) :
        threading.Thread.__init__(self)
        self.나의이름 = 나의이름

    def run(self) :
        for 숫자 in range(0,5) :
            print(self.나의이름, 숫자)

첫번째 = 스레딩숫자세기('첫번째')
두번째 = 스레딩숫자세기('두번째')

첫번째.start()
두번째.start()