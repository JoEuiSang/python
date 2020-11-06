def f1():
    print('bbb')


def f2():
    print('ccc')


def f3(a, b):
    return a + b


def select(f, params=None):
    # f: 함수의 참조값을 받아오는 파라메터, 핸들러 등록함수.
    # 핸들러: 이벤트가 발생하면 자동으로 호출되서 그 처리를 하는 함수
    # params=None : 디폴트 인자로 None을 지정, 생략 가능
    if params == None:
        f()
    else:
        f(params)



def f4(x):  # 파라미터로 튜플을 받음, 튜플: immutable요소로 갯수와,값 변경불가
    for i in x:
        print(i, end=' ')


def main():
    a = 1 + 5 * 6
    b = 112

    select(f1)
    select(f2)
    res = f3(a, b)
    print(res)

    f1()  # 함수를 호출하면 그 함수가 사용할 스택 메모리를 할당당

    # 파라미터가 있는 함수를 넘겨주기
    select(f4, (1, 2, 3))


main()

# if __name__ == '__main__':
