# 원본파일명과 타깃 파일명을 입력받아 복사하느 프로그램을 만드시오

# origin = input('원본 파일명 입력:')
# target = input('타겟 파일명 입력:')
#
# f1=open(origin,'r',encoding='utf-8')
# content = f1.read()
# f1.close()
# print(content)
# f2=open(target,'w',encoding='utf-8')
# f2.write(content)
# f2.close()
# f3=open(target,'r',encoding='utf-8')
# content=f3.read()
# print()

### 키보드로 입력받은 내용을 파일에 저장하시오
filename = input('파일명 입력')
# 파일 쓰기모드 오픈
# ocreate : 파일이 있으면 그파일 오픈 없으면 생성 , 기호 'a'
# otruncate : 기존내용 삭제, 기호 '
file = open(filename, 'a', encoding='utf-8')

while True:
    line = input('입력')
    if line == '/stop':
        break
    file.write(line + '\n')

file.close()

with open(filename, 'r',encoding='utf-8') as f:
    content = f.read()

print(content)


# rb / wb/ ab / rt / wt
'''
rb : 바이너리 읽기
wb : 바이너리 쓰기
ab : 바이너리 이어쓰기
'''
'''
r+: 읽고쓰기모드 ,없는파일열면 에러
w+: 읽고쓰기모드 , 없는파일 열면 새로 생성하여 오픈, 기존파일이 있으면 삭제후 새로 생성
a+: 읽고쓰기모드 , 없는파일은 새로생성, 기존파일 있으면 이어쓰기
'''