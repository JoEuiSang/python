# 3명 학생의 이름,번호 , 국, 영, 수 , 점수를 입력받아 총점, 평균을 출력하고, 총점순으로 정렬하여 출력하시오

st = [[0 for col in range(7)] for row in range(3)]
title = ['이름', '번호', '국어', '영어', '수학']
for i in range(len(st)):
    for idx, value in enumerate(title):
        if idx == 0:
            st[i][idx] = input(value)
            continue
        st[i][idx] = int(input(value))

for i in range(len(st)):
    sum = 0
    for j in range(2, 5):
        sum += st[i][j]
    avg = sum / 3
    st[i][5] = sum
    st[i][6] = avg
    print(st[i][0], ' 학생', '총점:', sum, '평균:', avg)

# 과제 : 총점 등수대로 출력 해오기

max = 0
count = 0

for i in range(1, len(st)):  # 키값
    for j in range(i, 0, -1):
        if st[j - 1][5] < st[j][5]:  # 앞쪽이 크면 스왑
            # print("스왑")
            st[j], st[j - 1] = st[j - 1], st[j]
        else:
            break

for i in range(len(st)):
    print(st[i][0], ' 학생', '총점:', st[i][5], '평균:', st[i][6])
