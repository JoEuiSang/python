import math

size = int(input("사이즈 입력"))

#왼쪽직각삼각형
for i in range(0, size + 1):
    for j in range(0, i):
        print("*", end='')
    print()

#오른쪽직각삼각형
for i in range(0, size + 1):
    space = size - i
    #공백 출력
    for j in range(0, space):
        print(end=" ")
    #별출력
    for j in range(0, i):
        print("*", end='')
    print()

print()
#피라미드
for i in range(0, size + 1, 2):
    space = math.floor((size - i)/2)
    #공백 출력
    for j in range(0, space):
        print(end=" ")
    #별출력
    for j in range(0, i+1):
        print("*", end='')
    print()
