def f1(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=' ')

def f2(num):
    res = []
    for i in range(1,num+1):
        if num%i==0:
            res.append(i)

    return res

f1(25)
print(f2(100))