class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self,name,age,hobby):
        super().__init__(name, age)
        self.hobby = hobby

def main():
    c= Child('aaa',12,'드럼')
    print('c.name:',c.name,'c.age:',c.age,'c.hobby:',c.hobby)

main()