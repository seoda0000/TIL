def draw(n):
    if n == 3:
        return [
            [' ', ' ', '*', ' ', ' '],
            [' ', '*', ' ', '*', ' '],
            ['*', '*', '*', '*', '*']
        ]

    last = draw(n // 2)
    res = []
    bcnt = (len(last[0]) // 2) + 1
    for l in last:
        res.append([' '] * bcnt + l + [' '] * bcnt)
    for l in last:
        res.append(l + [' '] + l)
    return res


N = int(input())
arr = draw(N)

for a in arr:
    print(''.join(a))
