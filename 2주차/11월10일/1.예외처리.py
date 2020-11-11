'''
예외 : 프로그램 런타임시 발생하는 문제. 보통 예외가 발생하면 프로그램은 중단

예외처리는 예외가 발생하더라도 프로그램이 중단되는 것을 막는다

try:
    예외가 발생할만한 코드
except 예외명 :
    try 블록에서 발생한 예외 중 동일한 일므의 예외만 받아서 처리
else:
    try 블록에서 예외가 발생하지 않았을 때 실행될 코드 구현
finally:
    정상종료, 비성상종료 모두 종료 되기전 실행되는 블록

'''

a = int(input('a:'))
b = int(input('b:'))
c = [1, 2, 3]
d = {'name': 'aaa', 'age': 12}

print('0으로 나누기 전')
print('위에서 중단되면 여기는 출력안됨')
# print(a / b) #에러출력 0으로 나누기 불가

try:
    print('try 블록 시작')
    print(a / b)
    print(d['tel'])

except ZeroDivisionError:
    print('0으로 나누면 안됩니다')
    try:
        c[3] = 10
    except IndexError:
        print('인덱스가 없습니다')

except KeyError:
    print('없는 Key 입니다')

except : #위에 캐치한 except 외의 모든 예외를 처리
    print('따로 선언하지 않은 예외 처리')

else:
    print('예외가 발생하지 않았습니다')

finally:
    print('끝')

# except (에러1,에러2,에러3):  처리방식이 동일하다면 이런식으로 처리해도 된다.