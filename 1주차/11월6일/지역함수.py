def f1(x):
    if x=='windows':
        def win():
            print('윈도우즈 입니다')
    elif x=='linux':
        def linux():
            print('리눅스 입니다')
    else:
        def other():
            print('다른 종류의 os입니다')


    # win()
    linux()
    # other()

def main():
    # win()
    # linux()
    # other()

    f1('linux')

main()