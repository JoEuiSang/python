'''
100개 출력
1재귀
2루프
3리스트
'''


# 재귀 피보나치
def fibo(num):
    if num <= 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


# for i in range(1, 101):
#     print(fibo(i), end=' ')


# 루프 피보나치
def fibo2(num):
    cur = 1
    num1 = 1
    num2 = 1
    while cur <= num:
        if cur == 1 or cur == 2:
            print(1, end=' ')
        else:
            sum = num1 + num2
            num1 = num2
            num2 = sum
            print(sum, end=' ')
        cur += 1


# 리스트 피보나치
def fibo3(num):
    list = [0] * (num)
    list[0] = 1
    list[1] = 1
    for i in range(2, 100):
        list[i] = list[i - 1] + list[i - 2]

    for i in range(0, 100):
        print(list[i], end=' ')


# fibo(100) 오래걸림
fibo2(100)
print()
fibo3(100)