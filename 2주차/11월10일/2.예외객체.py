# raise : 예외 객체를 던짐

class MyError(Exception):  # Exception 파이썬에서 모든 예외의 조상 클래스
    def __init__(self, msg):    # __init__ : 생성자, 객체 생성시 한 번 호출되는 함수로 객체를 초기화
                                # self: 현재 객체의 참조값 this와 같은 의미
        #멤버변수  = 파라미터       파라미터는 init 함수의 지역변수, 멤버변수는 MyError객체의 지역변수
        self.msg = msg


def printNum():
    num = int(input('num(1~5) 사이 입력:'))

    if num < 1 or num > 5:
        raise MyError('잘못된 값')

    print('input value :', num)


def main():
    try:
        printNum()
        a=[]
        a[1]=1
    except MyError as e:        #에러 객체 던져진 것을 e로 정의함
        print('예외발생 :', e.msg)
    except Exception as e:
        print('모든 예외 처리')
        print(e)


main()
