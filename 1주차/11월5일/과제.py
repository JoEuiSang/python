'''
1번과제
빈 리스트를 하나 만들어서
메뉴:추가(중복금지), 검색, 수정, 삭제, 전체목록, 전체삭제, 종료


2번과제 : 주소록
[[이름, 전화, 주소],[],[]]

이름중복 금지
메뉴:추가,검색,수정,삭제,전체목록,전체삭제,종료
이름 기준으로 검색, 중복체크, 수정, 삭제

'''

list1 = []


# def dup_check(num):
#     if num in list1:
#         return True

def add_list():
    num = int(input('추가할 값 입력 : '))
    if num in list1:
        print('이미 있는 값 입니다')
        return
    list1.append(num)
    return


def search_list():
    num = int(input('검색할 값 입력 : '))
    if num in list1:
        print(list1.index(num), '번째에 있습니다.')
        return
    else:
        print('없는 값 입니다')


def update_list():
    before = int(input('수정 전 값 입력 : '))
    if before in list1:
        after = int(input('수정 후 값 입력 : '))
        list1[list1.index(before)] = after
        return
    else:
        print('없는 값 입니다')


def delete_list():
    num = int(input('삭제할 값 입력 : '))
    if num in list1:
        list1.remove(num)
        return
    else:
        print('없는 값 입니다')


def select_all_list():
    for idx, i in enumerate(list1):
        print(f'{idx}번 : {i}')


def delete_all_list():
    list1.clear()
    print('모든요소가 삭제되었습니다')


# 주소록 관련함수 시작

addr = []


def add_addr():
    n = input('이름 입력 : ')
    for item in addr:
        if n == item[0]:
            print('이미 있는 값 입니다')
            return

    t = input('전번 입력 : ')
    a = input('주소 입력 : ')

    addr.append([n, t, a])
    return


def search_addr():
    n = input('검색할 이름 입력 : ')
    for idx, item in enumerate(addr):
        if n == item[0]:
            print(idx, '번째에 있습니다.')
            print(f'이름 : {item[0]}, 전화번호 : {item[1]}, 주소 : {item[2]}')
            return

    print('없는 이름 입니다')


def update_addr():
    before = input('수정할 이름 입력 : ')
    for idx, item in enumerate(addr):
        if before == item[0]:
            t = input('수정할 전화번호 입력 : ')
            a = input('수정할 주소 입력 : ')
            addr[idx][1] = t
            addr[idx][2] = a
            return
    print('없는 이름 입니다')


def delete_addr():
    name = input('삭제할 이름 입력 : ')
    for idx, item in enumerate(addr):
        if name == item[0]:
            del addr[idx]
            return
    else:
        print('없는 이름 입니다')


def select_all_addr():
    if len(addr) == 0:
        print('등록된 정보가 없습니다')
        return

    for item in addr:
        print(f'이름 : {item[0]}, 전화번호 : {item[1]}, 주소 : {item[2]}')


def delete_all_addr():
    addr.clear()
    print('모든요소가 삭제되었습니다')


while True:
    menu = int(input('1번과제(리스트CRUD)\n2번과제(주소록CRUD)\n종료.0'))

    if (menu == 1):
        print('1번과제 리스트')
        f = [add_list,
             search_list,
             update_list,
             delete_list,
             select_all_list,
             delete_all_list]

        while True:
            sel = int(input('1.추가\n2.검색\n3.수정\n4.삭제\n5.전체출력\n6.전체삭제\n0.종료'))

            # 룩업테이블로하면 직관적이지 않은 느낌
            if sel == 1:
                f[0]()
            elif sel == 2:
                f[1]()
            elif sel == 3:
                f[2]()
            elif sel == 4:
                f[3]()
            elif sel == 5:
                f[4]()
            elif sel == 6:
                f[5]()
            elif sel == 0:
                break
            print()

    elif (menu == 2):
        print('2번과제 함수')
        while True:
            list = []
            sel = int(input('1.추가\n2.검색\n3.수정\n4.삭제\n5.전체출력\n6.전체삭제\n0.종료'))
            if sel == 1:
                add_addr()
            elif sel == 2:
                search_addr()
            elif sel == 3:
                update_addr()
            elif sel == 4:
                delete_addr()
            elif sel == 5:
                select_all_addr()
            elif sel == 6:
                delete_all_addr()
            elif sel == 0:
                break
            print()

    elif (menu == 0):
        break
