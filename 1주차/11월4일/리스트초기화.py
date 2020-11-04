a=[]
aa=[1,2,3,'dd']
aaa=['d']
b=[0]*100 # 0으로 구성된 100사이즈 배열

c=[[0]*3]*4
print(c)

# 숫자 10개 입력 받아 리스트에 담고
# 출력

list = [0]*10
for i in range(len(list)):
    list[i] = int(input("입력:"))

for i in list:
    print(i,end=" ")

#합 계산
s=0
for i in list:
    s+=i
    print(s, end=' ')