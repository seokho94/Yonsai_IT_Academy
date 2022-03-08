import factory.py_module as 공설
import factory.py_module_2 as 참치

공설.인사말출력()
print('공장설립은 {}에 했습니다.'.format(공설.공장설립연도))

참01호 = 참치.참치선물세트(12, 3, 3)
참01호.출력('참치선물세트 01호')