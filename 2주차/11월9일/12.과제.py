'''
메모장 : 프로그램
1.읽기 : 파일 읽기
2.쓰기 : 파일명 입력, 중복 X
3.삭제 : 파일목록 보여줌, 삭제할 파일 선택 -> 파일 삭제
4.clear : 메모 디렉토리 전체 삭제
5.종료
'''
import os

workDir = './Memo'

def remove():
    list = os.listdir(workDir)
    for (idx, i) in enumerate(list):
        print(f'{idx}번 파일:{i}')

    idx = int(input('삭제할 파일을 선택하세요'))

    path = workDir + '/' + list[idx]
    print(path, '를 삭제합니다')
    os.remove(path)

def rmdir():
    yn = input('폴더를 삭제할까요?')
    if yn == 'y':
        os.rmdir(workDir)
        print('폴더가 삭제되었습니다')

def read():
    list = os.listdir(workDir)
    for (idx, i) in enumerate(list):
        print(f'{idx}번 파일:{i}')

    idx = int(input('읽을 파일을 선택하세요'))

    path = workDir + '/' + list[idx]
    print(path)
    f = open(path, 'r', encoding='utf-8')
    f.seek(0, 0)
    content = f.read()
    print(content)

def write():
    f_name = input('파일명 입력')
    path = workDir + '/' + f_name

    if os.path.isfile(path):  # 파일 존재하면
        print('파일이 존재합니다')
        yn = input('이어쓰기 y\n새로입력 n')
        if yn == 'y':
            print('이어서 작성합니다')
            f = open(path, 'a+', encoding='utf-8')
            while True:
                content = input('내용입력(종료 q:) : ')
                if content == 'q:': break
                f.write(content)
            f.close()

        elif yn == 'n':
            print('내용을 삭제하고 새로 작성합니다')
            f = open(path, 'w+', encoding='utf-8')
            while True:
                content = input('내용입력(종료 q:) : ')
                if content == 'q:': break
                f.write(content)
            f.close()

    else:  # 파일이 없으면
        print('파일을 생성하고 새로 작성합니다')
        f = open(path, 'w', encoding='utf-8')
        while True:
            content = input('내용입력(종료 q:) : ')
            if content == 'q:': break
            f.write(content)
        f.close()


def main():
    if (os.path.isdir(workDir) == False):
        os.mkdir(workDir)

    while True:
        sel = int(input('1.읽기 2.쓰기 3.삭제 4.clear 5.종료'))

        if sel == 1:
            read()
        elif sel == 2:
            write()
        elif sel == 3:
            remove()
        elif sel == 4:
            rmdir()
        elif sel == 5:
            break


main()
