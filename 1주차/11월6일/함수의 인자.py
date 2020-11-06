'''
1.요구인자 : 함수에서 일반적으로 사용하는 방법으로 파라메터 개수와 순서를 맞추어 호출
2.키워드인자:파라메터 순서에 맞추지 않아도됨, 단 이 인자가 어느 파라메터로 전달될지 지정해야함
3.디폴트인자: 파라메터 기본값을 지정하여 생략가능
4.가변인자: 파라메터의 개수 가변. 인자값을 튜플에 담아 전달
'''

def arg1(name, tel, age): #요구인자
    print('name:',name)
    print(f'tel: {tel}')
    print(f'age: {age}')
    print('12년 후 age:',age+12)

def arg2(age,name='aaa',tel='111'): #디폴트인자
    print('name:', name)
    print(f'tel: {tel}')
    print(f'age: {age}')

def arg3(*nums): #가변인자. 파라메터는 전달한 값의 개수를 크기로한 리스트
    print(type(nums))
    for i in nums:
        print(i)

def main():
    '''
    '''
    arg1('aaa','111',12) #요구인자
    # arg1('bbb',12,'222') #에러발생

    #키워드 인자, 순서 바뀌어도 문제 없음
    arg1(tel='1234',age=12,name='aaa')

    #디폴트 인자
    arg2(12)
    arg2(22,'bbb')
    arg2(32,'ccc','4123')

    #가변인자
    arg3(1,2,3)
    arg3(10,20,30,40,50)


main()