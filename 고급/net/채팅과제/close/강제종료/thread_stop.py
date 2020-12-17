import threading, time


def th(flag):
    a = 0
    while True:
        if flag():
            break

        a += 1
        print(a)
    print('th stop')


def main():
    flag = False
    t = threading.Thread(target=th, args=(lambda: flag,))
    t.start()
    time.sleep(1)
    flag = True
    print('main stop')


main()
