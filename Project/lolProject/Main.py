import Project.lolProject.ChampionMenu as championMenu
import Project.lolProject.ItemMenu as itemMenu



def main():
    cham = championMenu.Menu()
    item = itemMenu.Menu()
    itemsvc = None
    while True:
        print('1. 챔피언 모드\n2. 아이템 모드\n0. 종료')
        sel = int(input())
        if sel == 1:
            cham.run(itemsvc)
        elif sel == 2:
            itemsvc = item.run()
        elif sel == 0:
            break

main()
