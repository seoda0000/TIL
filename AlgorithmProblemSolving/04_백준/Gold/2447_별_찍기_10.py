def draw(n):
    if n == 1:
        return [['*']]

    last = draw(n // 3)
    res = []
    for l in last:
        res.append(l * 3)
    for l in last:
        res.append(l + [' '] * (n // 3) + l)
    for l in last:
        res.append(l * 3)
    return res

N = int(input())
arr = draw(N)

for a in arr:
    print(''.join(a))