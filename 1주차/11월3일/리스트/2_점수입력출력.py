score = [0, 0, 0]

i = 0
while i < len(score):
    score[i] = int(input("점수 입력:"))
    i += 1

sum = sum(score)
avg = sum / len(score)

print("총점 : ", sum)
print("평균 : ", avg)

# for i in range(시작값, 마지막값(포함안함), 스텝)

print("평균보다 높은 점수")
for i in range(len(score)):
    if (score[i] > avg):
        print(score[i])

#최고점수
max = 0

for i in range(len(score)):
    if(score[i] >max):
        max=score[i]

print("최고점수 : ", max)