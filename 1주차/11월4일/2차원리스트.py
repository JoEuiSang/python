# 리스트는 요소의 타입에 제한이 없다
# 정수, 문자열, 리스트, 객체

arr = [[1, 2, 3], [4, 5, 6]]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()

print(arr[0])
print(arr[1])

list = [[0 for col in range(3)] for row in range(2)]

print(len(list[0]))
print(len(list[1]))
number = 1
for i in range(len(list)):
    print("d")
    for j in range(len(list[i])):
        print('i:', i, 'j:', j)
        list[i][j] = number
        number += 1

for i in list:
    print('i', i)
    for j in i:
        print(j, end=' ')
    print()

