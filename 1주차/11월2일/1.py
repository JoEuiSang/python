"""score = int(input("점수 입력 : "))

if score >= 60:
    print('합격')
else:
    print('불합격')
"""
# def add(x, y):
#    return x+y
#
# print(add(1,4))

"""number = int(input("숫자 입력 : "))
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")"""

# 성별 나이 입력받기 20세이상 여자만 입장가능
gender = input("성별입력(남/여) : ")
age = int(input("나이입력 : "))

if age >= 20 and gender == "여":
    print("입장가능")
else:
    print("입장불가")
