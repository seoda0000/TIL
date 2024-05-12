def draw(N):
    if N == 1:
        return ['*']
    arr = []
    bef = draw(N - 1)

    if N % 2 == 0:
        bef = bef[::-1]

    hb = len(bef)
    wb = len(bef[0])
    ha = hb * 2 + 1
    wa = wb + (2 * hb) + 2

    arr.append(' ' * (wa // 2) + '*' + ' ' * (wa // 2))

    for i in range(1, hb):
        arr.append(' ' * (wa // 2 - i) + '*'
                   + ' ' * (i * 2 - 1)
                   + '*' + ' ' * (wa // 2 - i))

    for i in range(hb, ha - 1):
        n = i - hb
        arr.append(' ' * (wa // 2 - i) + '*'
                   + ' ' * n
                   + bef[n]
                   + ' ' * n
                   + '*' + ' ' * (wa // 2 - i))
    arr.append('*' * wa)

    if N % 2 == 0:
        arr = arr[::-1]

    return arr


N = int(input())

arr = draw(N)
W = len(arr[0])
H = len(arr)
if N % 2:
    for i in range(H):
        print(arr[i][:W - (H - i) + 1])
else:
    for i in range(H):
        print(arr[i][:W - i])
