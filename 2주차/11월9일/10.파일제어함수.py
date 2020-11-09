'''
1) turncate(size) - size크기로 파일 절삭
2) rename(old, new) - 파일명을 old에서 new로 변경
3) remove(파일명) - 파일삭제
'''

#truncate
def main():
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    f = open('f.txt','w')
    f.write(str1)
    f.truncate(10)  #10 사이즈로 절삭
    f.close()

    f=open('f.txt','r')
    print(f.read())
    f.close()

#rename
import os # 임포트필요
def main2():
    old_name=input('바꾸고싶은파일:')
    new_name=input('바꿀파일이름:')

    os.rename(old_name,new_name)

    f=open(new_name,'r',encoding='utf-8')
    print(f.read())
    f.close()

#remove
import os # 임포트필요
def main3():
    f=open('rem.txt','w+')
    f.write('hello python')
    f.seek(0)
    print(f.read())
    f.close()

    os.remove('rem.txt')

    # # f=open('rem.txt','r') #파일이 없어서 에러발생
    # print(f.read())
    # f.close()



main2()