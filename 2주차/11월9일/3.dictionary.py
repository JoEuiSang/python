# 딕셔너리
'''
키와 값을 같이저장
요소의 추가,변경,삭제 가능
키는 중복, 변경 안됨.  키는 숫자, 문자열, 튜플만 가능
값을 중복, 변경 허용. 값의 탕비 제한 없음

'''

# 1.생성
# 키는 name,tel, age이고 값은 'aaa','111',15
d1 = {"name": "aaa", "tel": "111", "age": '15'}
print(d1)

d2 = dict()

# 2.요소접근

# 키값으로 요소접근
print(d1["name"])

# 루프로 키값을 꺼내 접근
for key in d1:
    print('key', key, '/ value', d1[key])

# items() 메서드로 요소 출력
# items는 각 요소를 키와 값으로 묶어 튜플로 만들고 이 튜플들을 리스트에 담아 반환

print(d1.items())

###요소 추가,수정,삭제

d1 = {}  # 빈 딕셔너리 추가
d1['name'] = 'aaa'
d1['tel'] = '111'
print(d1)

d1['name'] = 'bbb'  # 이미 존재하는 키로 값 추가하면 수정된다
print(d1)


d1={1:'aaa',2:'bbb',3:'ccc',4:'ddd',5:'eee',6:'fff'}
del d1[2] #키가 2인 요소 삭제
print(d1) #전체 요소 출려개보면 키가 2인 요소가 빠졌다

d1.pop(4) #키가 4인 요소 삭제, 값 추출
print(d1)

print(d1.popitem()) # 임의의 요소 하나 팝
print(d1)

d1.clear() #모든 요소 삭제
print(d1)

del d1 #딕셔너리 객체 삭제
# print(d1) #에러발생