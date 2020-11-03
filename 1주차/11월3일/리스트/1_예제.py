# 리스트 선언
arr = [1, 2, 3, 4, 5]

# 일반적인 노가다 출력
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# 리스트 추가
arr.append(10)

print(arr[5])

print(len(arr))

# 반복문으로 출력
i = 0
while arr.__sizeof__() > 0:
    print(arr[i])
    i += 1
