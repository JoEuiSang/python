def list_add(list):    return sum(list)


def list_avg(list):    return sum(list) / len(list)


def list_max(list):    return max(list)


def list_min(list):    return min(list)


def list_max_min(list):
    arr = []
    max_val = max(list)
    min_val = min(list)
    arr.append(max_val)
    arr.append(min_val)
    print(arr)
    return arr

num = [3, 8, 6, 1, 4, 9, 5, 12]

print(f"총합:, {list_add(num)}")
print('평균값:', list_avg(num))
print('최대값:', list_max(num))
print('최소값:', list_min(num))
res = list_max_min(num)
print(f'최대값 : {res[0]} 최소값: {res[1]}')

