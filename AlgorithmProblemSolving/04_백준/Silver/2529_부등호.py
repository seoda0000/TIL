def fill_num(nth):
    global mx, mn
    if nth == N + 1:
        num = int(''.join(map(str, temp)))
        mx = max(mx, num)
        mn = min(mn, num)
        return
    elif nth == 0:
        for i in range(10):
            temp[nth] = i
            v[i] = 1
            fill_num(nth + 1)
            v[i] = 0
    else:
        if signs[nth - 1] == '<':
            for i in range(temp[nth - 1] + 1, 10):
                if v[i]: continue
                temp[nth] = i
                v[i] = 1
                fill_num(nth + 1)
                v[i] = 0
        else:
            for i in range(temp[nth - 1]):
                if v[i]: continue
                temp[nth] = i
                v[i] = 1
                fill_num(nth + 1)
                v[i] = 0

    return


N = int(input())
signs = list(input().split())
mx, mn = 0, 10_000_000_000
temp = [0] * (N + 1)
v = [0] * 10
fill_num(0)
print(str(mx).rjust(N + 1, '0'))
print(str(mn).rjust(N + 1, '0'))
