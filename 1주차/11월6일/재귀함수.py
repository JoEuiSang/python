# 팩토리얼

# 재귀없는 일반적인 팩토리얼

num = int(input('노재귀 num:'))

res = 1

for i in range(1, num + 1):
    res *= i

print(res)


# 재귀 팩토리얼

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(int(input('재귀 num:'))))

