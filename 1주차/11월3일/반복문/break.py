# break는 반복문의 흐름을 중단하는 제어문으로
# 가장 가까운 반복을 중단시킬수 있다

score = -1

while score < 0 or score > 100:
    score = int(input("0~100사이 값 입력:"))

print(score)

while True:
    score = int(input("0~100사이 값 입력:"))
    if 0 <= score <= 100:
        break

print(score)
