# 요소=> 중복 허용 안함, 순서가 없다, 수정 불가능하다

# 1)생성  중괄호를 이용하여 생성

set1 = {1, 2, 3, 4}  # 가능
# set2={1,[2,3],4} #에러 출력, : 요소는 수정불가능한 값만 가능
print(set1)

list = [5, 6, 7, 8]
set3 = set(list)
print(set3)

# print(set3[1]) 에러 : set은 순서가 없다

set3.add(10)
set3.add(5)
set3.add('abc')
print(set3)  # 10은 추가되고 5는 중복이기때문에 추가 안됨
# {5, 6, 7, 8, 10}

set4 = {}  # 이렇게 생성하면
print(type(set4))  # dict 타입으로 생성된다

set5 = set()  # 이렇게 생성해야
print(type(set5))  # set 타입으로 생성된다

# 출력가능
for i in set3:
    print(i, end=' ')

print()

# 요소 여러개 추가
set3.update([11, 12, 13, 14])
print(set3)

# 검색
for i in set3:
    print(i, end=' ')
    if 3 in set3:
        print('found')
    else:
        print('not found')

print(len(set3))
# print(max(set3)) #//할수있지만 요소의 타입이 다르기때문에 비교불가
# print(min(set3))
# print(sum(set3))


# 요소의 삭제
set3.remove('abc')
print(set3)

print(max(set3))  # //할수있지만 요소의 타입이 다르기때문에 비교불가
print(min(set3))
print(sum(set3))

# set 무작위 요소 삭제
print(set3.pop())
print(f'set3: {set3}')

# set 전체요소 삭제
set3.clear()
print(f'set3: {set3}')

# set 자체를 삭제
del set3
# print(set3)


# 집합연산
# 합집합
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1 | set2  # 이렇게 합 가능
print(set3)

set4 = set1.union(set2)  # 이렇게 합 가능
print(set4)

# 교집합
set3 = set1 & set2  # 이렇게 합 가능
print(set3)
set4 = set1.intersection(set2)
print(set4)

# 차집합
set3 = set1 - set2
print(set3)
set4 = set2 - set1
print(set4)
set5 = set1.difference(set2)
print(set5)

# 대칭차집합  (A-B) U (B-A) = 1,2  U  5, 6
set3 = set1 ^ set2
print(set3)

# 합집합에서 교집합을 뺀 결과  대칭차집합이랑 똑같음
set4 = set1.symmetric_difference(set2)
print(set4)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b)) #true
print(b.issubset(a)) #false
print(a < b) #true
print(b < a) #false
print(b.issuperset(a)) #true