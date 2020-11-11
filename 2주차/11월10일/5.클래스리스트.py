class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def printPoint(self):
        print('(', self.x, ',', self.y, ')')


def main():
    points = [Point(1, 2),Point(3, 4),Point(5, 6)]
    for i in points:
        i.printPoint()
main()
