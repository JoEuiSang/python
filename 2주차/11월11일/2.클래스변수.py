class Test:
    # 모든 객체가 공유. 클래스이름.변수명 으로 사용
    x = 0  # 클래스 변수, 자바의 static 변수와 비슷

    def __init__(self): # 멤버 메서드
        self.y = 0  # 멤버변수, 객체 마다 생성되는 변수, 객체이름.변수명
        z = 0  # 지역 변수 init 함수가 끝나면 없어짐

    @staticmethod   # 어노테이션
    def printNum(): #클래스 메서드, 멤버변수 사용없고 상수값을 구현 < 객체 소속이 아닌, 클래스 소속 >
        print('정적 메서드')

def main():
    Test.printNum()
    t1 = Test()
    Test.x += 1
    t1.y += 1
    print('test.x:', Test.x, ', y:', t1.y)
    print('t1.x:', t1.x, ', y:', t1.y)

    t2 = Test()
    Test.x += 1
    t2.y += 1
    print('test.x:', Test.x, ', y:', t2.y)
    print('t2.x:', t2.x, ', y:', t2.y)

main()
