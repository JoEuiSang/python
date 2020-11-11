# 파이썬에서 private 변수 및 함수는 다음과 같이 변수 및 함수 앞에 "__"(두개)를 붙여 선언 할 수가 있다.

class Test:
    def __init__(self, x, y):
        self.x = x      #public : 클래스 밖에서 접근 가능
        self.__y = y  # private : 클래스 밖에서 접근 불가

    def printXY(self):
        print(f'x: {self.x}, y: {self.__y}')

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

def main():
    t1 = Test(10,20)
    t1.printXY()

    print('t1.x', t1.x)
    t1.setY(300)
    # print('t1.y', t1.__y)       #에러, 접근 불가
    print('t1.y', t1.getY())

main()

