import random

#선택정렬
# 리스트중 가장 작은값을 선택하여 맨 앞자리로 가져온다
# 남은 값들중 가장 작은값을 선택하여 다음 자리로 가져온다(반복)

list = [0] * 10

for i in range(len(list)):
    list[i] = random.randrange(1, 100)

count = 1
print("기본")
print(list, end=' ')
print()

for i in range(len(list)):
    min = i
    for j in range(i,len(list)):
        if (list[min] > list[j]): min = j
    if(i == j): continue
    print(i, "번", "젤 작은값 : ", list[min])
    tmp = list[min]
    list[min] =list[i]
    list[i]=tmp
    print(list, end=' ')
    print()
