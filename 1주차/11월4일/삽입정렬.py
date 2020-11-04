import random

# 키가되는 값를 선정하고 그 자리보다 앞쪽에 있는 수와 비교하여 키가되는 값이 더 작으면 비교한 수의 앞쪽에 삽입해주는 방식
# 리스트 5 3 1 4 2 이 있다
# 최초 키 설정 2번째 자리인 3
# 키값인 3과 앞쪽수 5를 비교 3 < 5 이며 더이상 비교할 값이 없기에 삽입 3 5 1 4 2
# 다음 키 설정 3번째 자리인 1
# 키값인 1과 앞쪽수 5를 비교 1 < 5 이지만 앞에 비교할 수 3이있기에 비교
# 1<3 이며 더이상 비교할 값이 없기에 삽입을 해준다 1 3 5 4 2
# 이때 값을 교환하는 방식이 아닌 삽입해주는 방식이다 키값을 임시변수에 저장한뒤,
# 키값보다 큰 값을 가진 앞의 수들을 한칸씩 뒤로 밀어 키값이 들어갈 자리를 확보한뒤 삽입하는 방식이다

list = [0] * 10

for i in range(len(list)):
    list[i] = random.randrange(1, 100)

count = 1
print("기본")
print(list, end=' ')
print()

for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                   list[j], list[j-1] = list[j-1], list[j]
            else:
                   break

        print(i,"회전")
        print(list, end=' ')
        print()

for i in range(len(list)):
    list[i] = random.randrange(1, 100)

count = 1
print("기본")
print(list, end=' ')
print()

for i in range(1,len(list)):
    tmp=list[i]
    j=i-1
    while j>=0 and list[j]>tmp:
       list[j+1]=list[j]
       j-=1
    j+=1
    list[j]=tmp

print(list)