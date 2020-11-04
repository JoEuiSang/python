# n = [4, 6, 9, 7, 5, 10, 32, 661, 49, 85]
# print(n)
#
# search_num = int(input('찾을 숫자 입력 : '))
#
# flag = False
# for idx, i in enumerate(n):
#     if i == search_num:
#         print(i, "는", idx, "번 인덱스에 있습니다")
#         flag = True
#         break
#
# if not flag:
#     print("없음")

# 이진탐색
binary = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]
target = int(input("찾을 값 입력:"))

start = 0
end = len(binary) - 1

while start <= end: #시작 위치아 끝위치가 역전되지 않은채 반복
    mid = (start + end) // 2 #중간위치 찾기
    if target == binary[mid]: #찾을값과 중간에있는 값이 같으면
        print(mid, "번째에 있다")
        break

    elif target < binary[mid]: #찾을값이 중간에있는 값보다 작으면
        end = mid - 1           #끝을 중간 앞 위치로 설정

    else:                #찾을값이 중간에있는 값보다 크면
        start = mid + 1 #시작을 중간 뒤 위치로 설정

if start > end : print("없음")
