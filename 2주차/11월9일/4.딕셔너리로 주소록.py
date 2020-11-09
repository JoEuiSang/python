# # student = {'번호': {'name', 'kor', 'eng', 'math', 'total', 'avg'}}
#
# student = {} #모든 학생의 정ㅇ보로 번호를 키로 사용한다.ㄴ
# keys = ['name', 'kor', 'eng', 'math', 'total', 'avg']
# for i in range(0, 3):
#     s = {}
#     num = int(input('num:'))
#
#     for j in range(0, 4):
#         total = 0
#         if j ==0:
#             s[keys[j]] = input(keys[j]+': ')
#             continue
#         s[keys[j]] = int(input(keys[j] + ': '))
#         total+=s[keys[j]]
#     s[keys[4]]=total
#     s[keys[5]]=total/3
#     student[num]=s
#
# for num in student:
#     print('num:', num, end=' / ')
#     s = student[num]
#     for i in s:
#         print(i, ':', s[i], end=' / ')
#     print()
#

address={}
address[1]={}
address[2]={}
address[3]=2
address[1]['name']='ddd'
address[1]['kor']=123123
address[2]['kor']=222222
print(address[1]['name'])
print(address[1]['kor'])

print(address[2]['kor'])

print(address[3])

