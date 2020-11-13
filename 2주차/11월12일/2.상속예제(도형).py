class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print('(', self.x, ', ', self.y, ')')


# 도형, 삼각형,사각형,원 등을 모두 포함하는 추상적인 개념
# 구체적인 개념(삼각형,사각형,원)에 상속을 해주기 위한 슈퍼클래스
# 좌표를 가지고있다, 그리는 동작  ... 이러한 공통적 특징을 부모클래스로 선언
class Shape:
    def __init__(self):
        self.points = []  # 포함관계, point는 shape의 좌표를 구성하는 클래스
        self.name = ''

    def draw(self):
        print(f'{self.name}을 그린다')


class Triangle(Shape):
    def __init__(self, p):  # p: 좌표 담은 리스트
        super().__init__()
        self.name = '삼각형'
        for j in p:
            self.points.append(j)

    # 오버라이딩, 재정의 : 부모로부터 상속받은 메서드를 현재 클래스에 적합하게 고쳐쓰는 것
    def draw(self):
        super().draw()  # 재정의 하기전인 부모의 메서드를 사용
        for p in self.points:
            p.printXY()


class Recangle(Shape):
    def __init__(self, p):  # p: 좌표 담은 리스트
        super().__init__()
        self.name = '사각형'
        for j in p:
            self.points.append(j)

    # 오버라이딩, 재정의 : 부모로부터 상속받은 메서드를 현재 클래스에 적합하게 고쳐쓰는 것
    def draw(self):
        super().draw()
        for p in self.points:
            p.printXY()


class Circle(Shape):
    def __init__(self, p, r):  # p: 좌표 3개를 담은 리스트
        super().__init__()
        self.name = '원'
        self.points.append(p)
        self.r = r

    # 오버라이딩, 재정의 : 부모로부터 상속받은 메서드를 현재 클래스에 적합하게 고쳐쓰는 것
    def draw(self):
        super().draw()
        print('중심점:')
        self.points[0].printXY()
        print('반지름:', self.r)


def main():
    t = Triangle([Point(1, 2), Point(1, 5), Point(3, 3)])
    t.draw()

    r = Recangle([Point(0, 1), Point(4, 3)])
    r.draw()

    c = Circle(Point(5, 5), 5)
    c.draw()


main()
