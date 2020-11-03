# 추가, 검색, 수정, 삭제, 전체출력, 종료

arr = []

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
        print("숫자 추가")
        arr.append(input("숫자 입력하세요"))

    elif sel == 2:
        print("숫자 검색")
        target = input("검색할 숫자 입력하세요")

        i = 0
        while i < len(arr):
            if arr[i] == target:
                print(arr[i], "는 ", i, "번에 있습니다.")
                break
            i += 1

        if (i == len(arr)):
            print(target, "는 없습니다.")

    elif sel == 3:
        print("숫자 수정")
        target = input("수정할 숫자를 입력하세요")

        i = 0
        while i < len(arr):
            if arr[i] == target:
                arr[i] = input("수정할 값을 입력하세요")
                print("수정되었습니다")
                break
            i += 1
        if (i == len(arr)):
            print(target, "는 없습니다.")

    elif sel == 4:
        print("숫자 삭제")
        target = input("삭제할 숫자를 입력하세요")

        i = 0
        while i < len(arr):
            if arr[i] == target:
                arr.pop(i)
                print("삭제되었습니다")
                break
            i += 1
        if (i == len(arr)):
            print(target, "는 없습니다.")

    elif sel == 5:
        i = 0
        while i < len(arr):
            print(arr[i], end=' ')
            i += 1

    elif sel == 0:
        break
