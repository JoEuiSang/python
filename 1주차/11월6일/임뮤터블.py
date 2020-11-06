def paramTest1(num,msg):
    # immutable param test
    print('변경전')
    print('num: ',num,',msg:',msg)
    num=300
    msg='함수안'
    print('변경후')
    print('num: ', num, ',msg:', msg)

def main():
    n=10
    m='main안'
    print('함수 호출전')
    print('n:',n,', m:',m)
    paramTest1(n,m)
    print('함수 호출 후')
    print('n:', n, ', m:', m)

main()