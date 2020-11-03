# 리스트 선언
arr = [1, 2, 3, 4, 5]

# 일반적인 노가다 출력
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# 리스트 추가
# arr.append(10)

#리스트 삭제
"""
clear() 모든 요소 삭제
pop() 지정한 위치 값을 삭제하고 삭제한 값 취득
remove() 지정한 위치 값과 같은 값을 검색후 처음 값을 삭제
del 위치 또는 범위를 지정 삭제
"""

print(arr[5])

print(len(arr))

# 반복문으로 출력
i = 0
while i<len(arr):
    print(arr[i])
    i += 1
