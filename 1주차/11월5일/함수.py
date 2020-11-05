def fun1():  # 함수 명명 규칙은 변수 명명규칙과 동일
    print('hello function')


def fun2(a, b):
    print(a, "+", b, '=', a + b)


def fun3(a, b):
    return a + b


fun1()
fun2(1, 2)
res = fun3(3, 4)
print('res:', res)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def dev(a, b):
    if b==0:
        print('0으로 나눌수 없습니다.')
        return None
    return a / b


# a=10
# b=5
# print(add(a,b))
# print(sub(a,b))
# print(mul(a,b))
# print(dev(a,b))


res = 0
while True:
    menu = int(input('1.add 2.sub 3.mul 4.dev 0.stop'))
    a = int(input('num1 : '))
    b = int(input('num2 : '))
    if menu == 1:
        res = add(a, b)
    elif menu == 2:
        res = sub(a, b)
    elif menu == 3:
        res = mul(a, b)
    elif menu == 4:
        res = dev(a, b)
    elif menu == 0:
        print('종료합니다')
        break
    print(res)