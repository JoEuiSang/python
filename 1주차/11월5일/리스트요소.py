#리스트 요소 범위 접근
#list[시작위치:끝위치:간격]    (끝위치의 앞에까지만 출력함)

list1 = list(range(1,11))

print(list1)
a=list1[3:7:1]
print(a)
b=list1[3:8:2]
print(b)

print(list1[0:4])
print(list1[0:4:2])

#리스트요소추가
#추가 append(값) : 맨뒤에 추가
c = [1,2,3,4]
print(c)
c.append(10)
print(c)

# 지정위치에 추가 insert(인덱스,값)
c.insert(1,100)
print(c)

#리스트의 수정
list = [1,2,3,4]
print(list)
list[1] = 100
print(list)

#리스트의 삭제
#del, remove, clear, pop

#del 인덱스 기준으로 삭제
list = [1,2,3,4]
print(list)
del list[1]
print(list)
del list[0:2]
print(list)

#remove(x)  첫번째로 나오는 x값을 찾아서 삭제
list = [4,3,2,1]
print(list)
list.remove(3)
print(list)
# list.remove(3) #없는값 삭제시 에러
list.remove(2)

# clear 전체항목 삭제, 변수자체는 남아있다
list1 = [1,2,3,4]
print(list1)
list1.clear()
print(list1)
del list1 #변수자체가 사라진다
# print(list1)  #에러발생

#pop() 마지막반환 후 요소 삭제
#pop(x) x번째 반환후 요소 삭제
list = [1,2,3,4]
print(list)
list.pop(1)
print(list)


#요소 검색   index(찾을값): 찾을값의 인덱스를 반환
list1=[1,2,3,4,5,10]
if 10 in list1:
    print('10은 목록 포함')
    idx = list1.index(10)
    print(idx,'번째에있다')
else:
    print('10은 목록에 포함 안됨')

#요소 정렬
list1=[9,4,1,3,6,5]
print(list1)
list1.sort()  #디폴트 오름차순정렬
print(list1)
list1.sort(reverse=True) #내림차순정렬
print(list1)

#문자열 정렬가능
list2 = ['fsd','qwe','qbc','asdf']
print(list2)

list2.sort()
print(list2)


# 리스트 복사
#
# 얕은복사1, 단순히 객체를 복제하여 동일하게 수정됨
# 가리키는 주소값을 복사한다
b=[1,2,3]
c=b
print(b)
print(c)
print(id(b))
print(id(c))
b[1]=100
print(b)
print(c)

# 얕은복사2 : 기본 자료형인 상수는 동시 변경이 되지 않는다
import copy
a=[1,2,3,4]
b=copy.copy(a)
print(a)
print(b)
print(id(a))
print(id(b))
a[1]=100
print(a)
print(b)

# 하지만 요소에 객체(리스트)가 있을시 동일한 참조값으로 복사가 되기때문에
# 수정시 동시에 수정이 된다(이것이 문제점)
a = [1, [1, 2, 3]]
b = copy.copy(a)    # shallow copy 발생
print(b)    # [1, [1, 2, 3]] 출력
b[0] = 100
print(b)    # [100, [1, 2, 3]] 출력,
print(a)    # [1, [1, 2, 3]] 출력, shallow copy 가 발생해 복사된 리스트는 별도의 객체이므로 item을 수정하면 복사본만 수정된다. (immutable 객체의 경우)

c = copy.copy(a)
c[1].append(4)    # 리스트의 두번째 item(내부리스트)에 4를 추가
c[1][0]=100  #리스트의 두번째 item의 첫번째를 100으로 수정
print(c)    # [1, [100, 2, 3, 4]] 출력
print(a)    # [1, [100, 2, 3, 4]] 출력, a가 c와 똑같이 수정된 이유는 리스트의 item 내부의 객체는 동일한 객체이므로 mutable한 리스트를 수정할때는 둘다 값이 변경됨

print('깊은복사')
#깊은복사
#복합객체를 새롭게 생성하고
# 그 안의 내용까지 재귀적으로 새롭게 생성하게 됩니다.
# 서로 영향을 주지않는다
a = [1, [1, 2, 3]]
b = copy.deepcopy(a)    # deep copy 실행
print(b)    # [1, [1, 2, 3]] 출력
b[0] = 100
b[1].append(4)
print(b)    # [100, [1, 2, 3, 4]] 출력
print(a)    # [1, [1, 2, 3]] 출력