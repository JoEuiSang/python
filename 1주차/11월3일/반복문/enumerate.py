data = [12, 42, 123, 22]

# 요소와 인덱스 동시에 리턴
for idx, i in enumerate(data):
    print("idx:", idx, "value:", i)

print()

#마지막 , 빼기
for idx, i in enumerate(data):
    if (idx == len(data) - 1):
        print(i)
    else:
        print(i, end=', ')
