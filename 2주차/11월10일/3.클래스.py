'''
클래스 : 타입 정의, 캡슐화(하나의 객체 정보를 하나로 묶음)
객체 : 프로그램으로 모델링 할대 구성 요소들(사람, 사물, 개념)

클래스 : 사용자가 직접 정의하는 타입
클래스 변수를 만들려면 먼저 클래스 정의

class 클래스이름 :
    def 함수(self):
        self.a=10

사람의 정보를 이름, 나이 3명
'''


# 클래스는 멤버변수와, 메서드로 구성
# 멤버변수 : 객체 안의 변수
# 메서드 : 클래스에서 정의한 함수, 첫 파라미터는 항상 self(객체 자신), 호출 할 때 이 파라미터는 전달 안함
class Person:
    def __init__(self, name, age):  # 생성자, 함수, 객체 생성시 호출되는 함수, 객체 초기화
        self.name = name
        self.age = age

    def printPerson(self):
        print(self.name)
        print(self.age)


class Member:
    def setData(self,name,tel):
        self.name = name
        self.tel = tel

    def printMember(self):
        print(self.name)
        print(self.tel)

def main():
    p1 = Person('aaa',12)
    # toString 함수에 의해서 출력이 됨, 객체를 설명하는 함수
    print(p1)
    p1.printPerson()
    p2 = Person('조의상', 13)
    p2.printPerson()

    m1 = Member()
    m1.setData('aaa',111)
    m2 = Member()
    m2.setData('bbb',222)
    m2.printMember()

    m3=m1               #얕은복사, 참조값 복사
    m1.name='abc'
    m3.printMember()
    m1.printMember()

main()