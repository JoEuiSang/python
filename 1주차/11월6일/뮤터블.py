def paramTest2(list1, list2):
    # mutalbe param test

    print('변경전')
    print('list1:', list1)
    print('list2:', list2)
    list1 = [100, 200]
    list2[0] = 10
    list2[2] = 30
    print('변경후')
    print('list1:', list1)
    print('list2:', list2)


def main():
    li1 = [1, 2, 3]
    li2 = [4, 5, 6, 7]
    print('함수 호출 전')
    print('li1:', li1)
    print('li2:', li2)
    paramTest2(li1, li2)
    print('함수 호출 후')
    print('li1:', li1)
    print('li2:', li2)


main()
