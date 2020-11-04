import random

# 버블정렬
# 2개씩 묶어 값을 비교한뒤 정렬을 하는 방법
# n=5인 리스트 5 3 4 1 2 가 있다면
# 5,3 비교 후 3 5 4 1 2      비교 1번
# 그 후 5 4 비교 후 3 4 5 1 2 비교 2번
# 그 후 5 1 비교 후 3 4 1 5 2 비교 3번
# 그 후 5 2 비교 후 3 4 1 2 5 비교 4번
# 이렇게 n-1번 비교를 했고, 이 과정을 다시 반복하여 정렬이 n^2번 비교하면 정렬완성

list = [0] * 10

for i in range(len(list)):
    list[i] = random.randrange(1, 100)

count = 1
print("기본")
print(list, end=' ')
print()
for i in range(len(list) - 1):
    for j in range(len(list) - 1 - i):
        if (list[j] > list[j + 1]):
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp

    print(count, "회전")
    count += 1
    print(list, end=' ')
    print()
