"""
1번: 구구단 한단 출력(단수 입력받아서)
3 * 1 = 3
3 * 2 = 6
...
...
...

이런식으로 출력

2번 : 구구단 2~9단까지 다 출력(출력 모양은 그대로

3번 :  1~100사이의 소수 출력
4번 : 왼쪽 직각삼각형 만들기(크기입력)
*
**
***
****
*****

5번 : 오른쪽직각삼각형 만들기(크기입력)
    *
   **
  ***
 ****
*****

6번 : 삼각형(트리모양) 크기는 밑변의 크기
  *
 ***
*****

"""

import math

while True:
    num = int(input("""선택하시오
    1번: 구구단 한단 출력(단수 입력받아서)
    2번 : 구구단 2~9단까지 다 출력
    3번 :  1~100사이의 소수 출력
    4번 : 왼쪽 직각삼각형 만들기
    5번 : 오른쪽직각삼각형 만들기
    6번 : 삼각형(트리모양)
    0번 : 종료  ------------------------ : """))
    if num == 0:
        print("종료합니다")
        break

    if num == 1:
        dan = int(input("몇단? : "))
        i = 1
        while i <= 9:
            print(dan, " * ", i, " = ", dan * i)
            i += 1

    elif num == 2:
        i = 2
        while i <= 9:
            print("---------", i, "단--------")
            j = 1
            while j <= 9:
                print(i, " * ", j, " = ", i * j)
                j += 1
            i += 1

    elif num == 3:
        ok = 0 #나눠진 횟수
        i = 1
        while i <= 100:
            j = 1
            while j <= i:
                if i % j == 0: #나눠지면
                    ok += 1 #증가
                    if ok > 2: #근데 2번 넘어가면 실수가아님
                        break
                j += 1
            if ok == 2:
                print(i, end=" ")
            i += 1
            ok = 0
        print()

    elif num == 4:
        size = int(input("크기입력:"))
        i = 1
        while i <= size:
            j = 1
            while j <= i:
                print("*", end='')
                j += 1
            print()
            i += 1

    elif num == 5:
        size = int(input("크기입력:"))
        loop = 1

        while loop <= size:
            space = size - loop  # 앞에 들어갈 공백의 크기 , 최초크기 size-1
            while space > 0:
                print(" ", end='')
                space -= 1

            j = 1
            while j <= loop:
                print("*", end='')
                j += 1
            print()
            loop += 1


    elif num == 6:
        size = int(input("밑변 크기입력:"))
        loop = 1
        space = math.floor(size / 2)  # 앞에 들어갈 공백의 크기 , 최초크기 size/2 버린값
        while loop <= size:
            spacetmp = space
            while spacetmp > 0:
                print(" ", end='')
                spacetmp -= 1

            j = 1
            while j <= loop:
                print("*", end='')
                j += 1
            print()
            loop += 2
            space -= 1

        print()
