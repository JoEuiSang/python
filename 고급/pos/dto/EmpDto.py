class EmpDto:
    def __init__(self, id=None, name=None, positionName=None, pw=None):
        self.id = id
        self.name = name
        self.pw = pw
        self.positionName = positionName

    def __str__(self):
        return '직원번호 : '+ str(self.id)+', 이름 : '+self.name+', 직급 : '+self.positionName