'''
튜플
변경불가, 요소자체는 변경 가능
고정된 집합 데이터를 저장, 요소를 추가, 삭제, 변경 안됨
인덱스로 접근가능

'''

# 생성
t1 = (1, 2, 3)
print(t1)

print(type(t1))
t1 = (1, 3.24, 'asdf', [5, 6, 7])
print(t1)

t2 = ((1, 2, 3,), (4, 5, 6))
print(t1)
print(t2)

t3 = tuple([1, 2, 3])
print(t3)

t4 = tuple({4, 5, 6})

t5 = tuple('asdf')

t6 = 12, 22, 34

t7 = 'aaa', 'bbb', 'ccc'

# 빈튜플생성
t1 = ()
t2 = tuple()

# 요소 하나짜리 튜플 생성
t1 = (1)  # 정수
t2 = (1,)  # 튜플
t3 = ('abc')  # 정수
t4 = ('abc',)  # 튜플
t5 = 1  # 정수
t6 = 1,  # 튜플

# 초기화해서 만들기
t5 = (1,) * 3
print(t5)
t6=('hello', ) * 2
print(t6)

### 요소접근
#   t1[0] ~ t1[4]
t1 = (1, 2, 3, 4, 5)
#   t1[-5[ ~ t1[-1]

#정방향요소
for i in t1:
    print(i)

#정방향 인덱스
for i in range(0,len(t1)):
    print(t1[i])

# 역방향 인덱스
for i in range(len(t1)-1,-1,-1):
    print(t1[i])

#함수
'''
len() 길이
sum() 요소의 총합
max, min 최대값, 최소값
'''

#접근 인덱스 슬라이스
t4 = 1,2,3,4,5,6,7
print(f't4: {t4}')
print(f't4[2:5]: {t4[2:5]}')
print(f't4[:5]: {t4[:5]}')
print(f't4[2:]: {t4[2:]}')
print(f't4[:]: {t4[:]}')

t4 =([],)
print(t4)
t4[0].append(1)
t4[0].append(2)
t4[0].append(3)
print(t4)

#튜플의 활용
#여러 변수를 한꺼번에 초기화
a,b,c=1,2,3
print(a,b,c)