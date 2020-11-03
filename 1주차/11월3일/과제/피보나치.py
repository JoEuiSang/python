# 1. 피보나치 수열

fibonacci = [1,1]

for i in range(2,100):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

for i in fibonacci:
    print(i,end=' ')