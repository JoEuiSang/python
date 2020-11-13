'''
변수 : 소문자
상수 : 대문자
킄ㄹ래스명 : 첫글자대문자 나머지 소문자

생성자: 멤버변수정의
'''


class A:
    def __init__(self, a):
        self.a = a

    def methodA(self):
        print('methodA')


class B:
    def __init__(self, b):
        self.b = b

    def methodB(self):
        print('methodB')


class C:
    def __init__(self, c):
        self.c = c

    def methodC(self):
        print('methodC')


class D(A, B, C):
    def __init__(self, a, b, c, d):
        A.__init__(self,a)      #부모 A클래스의 생성자 호출
        B.__init__(self,b)      #부모 B클래스의 생성자 호출
        C.__init__(self,c)      #부모 C클래스의 생성자 호출
        self.d = d

    def methodD(self):
        print('methodD')
        print('a:',self.a)
        print('b:', self.b)
        print('c:', self.c)
        print('d:', self.d)


def main():
    d = D(1,2,3,4)
    d.methodA()
    d.methodB()
    d.methodC()
    d.methodD()


main()
