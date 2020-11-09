'''
tell() 현재 읽고 쓸 위치 반환

seek(off, whence): whence부터 off만큼 떨어진 곳
whence
0 : 맨앞 기준 , 1: 현재위치 기준, 2 :맨뒤기준
'''


def main2():
    f = open('ㅊ.txt', 'w', encoding='utf-8')
    str1 = '123456789abcdef123456'
    f.write(str1)
    f.close()

    f = open('ㅊ.txt', 'rb')
    print(f.read(9))
    print('현재위치:', f.tell())

    f.seek(5)
    print('현재위치:', f.tell())
    print('맨앞에서 5위치의 문자:', f.read(1))

    f.seek(10, 0)
    print('현재위치:', f.tell())
    print('맨앞에서 10위치의 문자:', f.read(1))

    f.seek(3, 1)
    print('현재위치:', f.tell())
    print('현재에서 3위치의 문자:', f.read(1))

    f.seek(-3, 1)
    print('현재위치:', f.tell())
    print('현재에서 -3위치의 문자:', f.read(1))

    f.seek(-3, 2)
    print('현재위치:', f.tell())
    print('맨뒤에서 -3위치의 문자:', f.read(1))


# main2()


# 역순으로 다른파일에 쓰기
def main3():
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    f = open('a.txt', 'w')
    f.write(str1)
    f.close()

    f1 = open('a.txt', 'rb')
    f2 = open('b.txt', 'w')
    for i in range(1, len(str1)+1):
        f1.seek(-i, 2)
        # print(str(f1.read(1))) # b'z' 이런식으로 출력이 되기때문에
        ch = str(f1.read(1)).split('\'')[1]  #리스트형식으로 바꿔서 1번방의 값을 넣어줌
        f2.write(ch)

    f1.close()
    f2.close()

    f1 = open('b.txt', 'r', encoding='utf-8')
    content = f1.read()
    print(content)


main3()
