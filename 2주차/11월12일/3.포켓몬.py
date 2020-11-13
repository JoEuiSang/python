class PocketMon:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.exp = 0
        self.level = 1

    def eat(self):
        print(f'{self.name} 이(가) 밥을 먹는다')

    def sleep(self):
        print(f'{self.name} 이(가) 잠을 잔다')

    def exercise(self):
        print(f'{self.name} 이(가) 운동을 한다')

    def play(self):
        print(f'{self.name} 이(가) 논다')

    def print(self):
        print(f'이름 {self.name}')
        print(f'레벨 {self.level}')
        print(f'체력 {self.hp}')
        print(f'경험치 {self.exp}')

    def levelUp(self):
        print(self.name, '의 레벨이 증가하여', self.level, '레벨이 되었습니다')

    def hpUp(self, up):
        if up > 0:
            print(self.name, '의 체력이', up, '증가하여', self.hp, '가 되었습니다')
        else:
            print(self.name, '의 체력이', -up, '감소하여', self.hp, '가 되었습니다')

    def expUp(self, up):
        print(self.name, '의 경험치가', up, '증가하여', self.exp, '가 되었습니다')

    def checkLv(self):
        if self.exp > 50:
            self.exp = 0
            self.level += 1
            self.levelUp()


class Picachu(PocketMon):
    def __init__(self):
        super().__init__()
        self.name = '피카츄'
        self.hp = 50

    def 백만볼트(self):
        print('백만볼트 공격')

    def eat(self):
        super().eat()
        up = 10
        self.hp += up
        self.hpUp(up)

    def sleep(self):
        super().sleep()
        up = 30
        self.hp += up
        self.hpUp(up)

    def exercise(self):
        super().exercise()
        up = 30
        self.exp += up
        self.expUp(up)
        self.checkLv()

    def play(self):
        super(Picachu, self).play()
        up = 30
        self.exp += up
        down = -20
        self.hp += down
        self.expUp(up)
        self.hpUp(down)
        self.checkLv()


class Pyree(PocketMon):
    def __init__(self):
        super().__init__()
        self.name = '파이리'
        self.hp = 60

    def 불꽃세례(self):
        print('불꽃세례 공격')

    def eat(self):
        super().eat()
        up = 20
        self.hp += up
        self.hpUp(up)

    def sleep(self):
        super().sleep()
        up = 10
        self.hp += up
        self.hpUp(up)

    def exercise(self):
        super().exercise()
        up = 20
        self.exp += up
        self.expUp(up)
        self.checkLv()

    def play(self):
        super().play()
        up = 10
        self.exp += up
        down = -30
        self.hp += down
        self.expUp(up)
        self.hpUp(down)
        self.checkLv()


class Isanghaessi(PocketMon):
    def __init__(self):
        super().__init__()
        self.name = '이상해씨'
        self.hp = 100

    def 넝쿨채찍(self):
        print('넝쿨채찍 공격')

    def eat(self):
        super().eat()
        up = 5
        self.hp += up
        self.hpUp(up)

    def sleep(self):
        super().sleep()
        up = 10
        self.hp += up
        self.hpUp(up)

    def exercise(self):
        super().exercise()
        up = 20
        self.exp += up
        self.expUp(up)
        self.checkLv()

    def play(self):
        super().play()
        up = 40
        self.exp += up
        down = -100
        self.hp += down
        self.expUp(up)
        self.hpUp(down)
        self.checkLv()


def main():
    sel = int(input('1.피카츄, 2.파이리, 3.이상해씨'))
    ch = None
    if sel == 1:
        ch = Picachu()      #업캐스팅(다형성)
    elif sel == 2:
        ch = Pyree()
    elif sel == 3:
        ch = Isanghaessi()

    ch.eat()
    ch.print()
    ch.exercise()
    ch.print()
    ch.sleep()
    ch.print()
    ch.play()
    ch.print()
    # isinstance(a,type) : a가 type인지 확인
    if isinstance(ch, Picachu):
        ch.백만볼트()
    elif isinstance(ch, Pyree):
        ch.불꽃세례()
    elif isinstance(ch, Isanghaessi):
        ch.덩쿨채찍()


main()
