student1 = int(input("점수입력:"))
student2 = int(input("점수입력:"))
student3 = int(input("점수입력:"))

sum = student1+student2+student3
aver = sum/3

print("평균 ",aver,"점")

if student1>aver:
    print("1번학생 : ",student1,"점")
if student2>aver:
    print("2번학생 : ",student2,"점")
if student3>aver:
    print("3번학생 : ",student3,"점")