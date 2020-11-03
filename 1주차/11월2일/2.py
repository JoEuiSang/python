score = int(input("점수 입력: "))

while score<0 or score>100:
    score = int(input("점수 입력: "))


if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
