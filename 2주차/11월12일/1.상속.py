# 클래스의 변수와 메서드를 물려받는 것
# 1.코드의 재사용성을 높이기위해
# 2.다형성을 구현하기 위해
# 3.조립형

# 하위 클래스들의 공통점을 추출하여 상위 클래스에 정의

class Parent:
    def __init__(self):
        self.x = 0
        self.y = 0
        print('부모생성자')

    def setData(self, x, y):
        self.x = x
        self.y = y

    def parentMethod(self):
        print('부모메서드')

    def printXY(self):
        print('x:', self.x, ' y:', self.y)


class Child(Parent):
    def __init__(self):
        # super().__init__()      #부모클래스의 생성자 호출, super() : 상속관계에서 부모객체 참조값 반환
        print('자식생성자')
        self.z = 0

    #메서드 재정의 필요. 상속받은 메서드 고쳐사용 overriding
    def setZ(self, z):
        self.z = z

    def z(self):
        print(self.x)

    def printXYZ(self):
        print('x:', self.x, ' y:', self.y,'z:',self.z)

    def childMethod(self):
        print('자식메서드')

def main():
    p = Parent()
    p.setData(1,2)
    p.printXY()
    p.parentMethod()

    c = Child()
    print(c.x)
    c.setData(30,20)
    c.setZ(100)
    c.printXYZ()
    print(c.x, c.y)
    c.parentMethod()
    c.childMethod()

main()