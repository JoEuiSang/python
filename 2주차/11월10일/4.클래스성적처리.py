class Student:
    def __init__(self, name, num, kor, eng, math):
        self.math = math
        self.eng = eng
        self.kor = kor
        self.num = num
        self.name = name

    def calc(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printInfo(self):
        print('name:', self.name)
        print('num:', self.num)
        print('kor:', self.kor)
        print('eng:', self.eng)
        print('math:', self.math)
        print('total:', self.total)
        print('avg:', self.avg)
        print('=============')


class Dao:  # DB작업 전담 클래스, 저장소에 추가, 검색, 수정, 삭제 등의 작업 수행
    def __init__(self):
        self.datas = []

    def insert(self, s):  # self.datas:멤버변수(리스트).
        self.datas.append(s)  # 파라미터로 받은 Student 객체 s를 리스트 (self.datas)에 추가

    def selectAll(self):
        return self.datas


class Service:  # 사용자에게 제공할 기능을 담당하는 객체
    def __init__(self):
        self.dao = Dao()

    def addStudent(self):  # 학생 정보를 추가
        name = input('name:')
        num = int(input('num:'))
        kor = int(input('kor:'))
        eng = int(input('eng:'))
        math = int(input('math:'))

        s = Student(name, num, kor, eng, math)  # vo 생성
        s.calc()
        self.dao.insert(s)

    def printAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printInfo()


def main():
    service = Service()
    service.addStudent()
    service.addStudent()
    service.addStudent()
    service.printAll()


main()

''' 
vo : value object   : 값을 담는 객체
dto : data transfer object  : 값을 담는 객체
vo == dto

MVC 패턴 = model, view, controller
model = 데이터, 비즈니스 (VO, DAO, Service)
view = UI 
controller = 연결부, 제어부
'''
