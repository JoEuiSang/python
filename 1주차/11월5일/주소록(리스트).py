member = []
member1 = []

# n = input('name:')
# t = input('tel:')
# a = input('address:')
# member.append([n, t, a])
#
# n = input('name:')
# t = input('tel:')
# a = input('address:')
# member.append([n, t, a])
#
# n = input('name:')
# t = input('tel:')
# a = input('address:')
# member.append([n, t, a])
#
# print(member)


# 함수: 코드를 모듈화 해서 필요할때마다 호출하여 사용하는 방법

def make_mem(): #함수선언
    global member1
    n = input('name:')
    t = input('tel:')
    a = input('address:')
    member1.append([n, t, a])


make_mem()

print(member1)
make_mem()
print(member1)
make_mem()
print(member1)
