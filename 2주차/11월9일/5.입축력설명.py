def main():
    # open(파일경로, 읽기쓰기모드, 형식)
    f = open("test.txt", "r", encoding='utf-8')
    content = f.read()
    print(content)
    f.close()

def main2():
    f = open('test.txt','r',encoding='utf-8')
    while True:
        str1 = f.read(3)
        if str1=='':
            break
        print(str1)
    f.close()

def main3():
    f = open('test.txt','r',encoding='utf-8')
    while True:
        str1 = f.readline()
        if str1=='':
            break
        print(str1)
    f.close()


def main4():
    with open('test.txt','r',encoding='utf-8') as f:
        str1 = f.read()
        print(str1)

# main4()

## 파일 쓰기 예제
def main5():
    f=open('c.txt','w')
    str1=input('파일에 작성할 내용을 입력하라')
    f.write(str1)
    f.close()
    f=open('c.txt','r')
    str1=f.read()
    print(str1)
    f.close()

main5()

