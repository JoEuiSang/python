class AddressBook:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def update(self, phone, addr):
        self.phone = phone
        self.addr = addr

    def select(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone)
        print("주소 : ", self.addr)

#주소록을 저장할 리스트변수
info = []

while True:
    print("""
    1.추가
    2.검색(이름)
    3.수정
    4.삭제(이름)
    5.전체출력
    0.종료
    """)
    sel = int(input("선택"))

    if sel == 1:
        print("주소록 추가")
        name = input("이름을 입력하세요")
        phone = input("전화번호를 입력하세요")
        addr = input("주소를 입력하세요")
        info.append(AddressBook(name, phone, addr))
        print(len(info))

    elif sel == 2:
        print("주소록 검색")
        name = input("검색할 사람의 이름을 입력하세요")

        i = 0
        while i < len(info):
            if info[i].name == name:
                info[i].select()
                break
            i+=1

    elif sel == 3:
        print("주소록 수정")
        name = input("수정할 사람의 이름을 입력하세요")
        phone = input("전화번호를 입력하세요")
        addr = input("주소를 입력하세요")

        i = 0
        while i < len(info):
            if info[i].name == name:
                info[i].update(phone, addr)
                print("수정되었습니다")
                break
            i+=1

    elif sel == 4:
        print("주소록 삭제")
        name = input("삭제할 사람의 이름을 입력하세요")

        i = 0
        while i < len(info):
            if info[i].name == name:
                info.pop(i)
                print("삭제되었습니다")
                break
            i+=1

    elif sel == 5:
        i = 0
        while i < len(info):
            print("-----", i + 1, "번------")
            print("이름 : ", info[i].name)
            print("전화번호 : ", info[i].phone)
            print("주소 : ", info[i].addr)
            print()
            i += 1

    elif sel == 0:
        break
