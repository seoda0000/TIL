def solve(mxk):
    for k1 in range(1, mxk + 1):
        for k2 in range(1, mxk + 1):
            if switch_card(k1, k2):
                return k1, k2


def switch_card(k1, k2):
    lst = list(range(1, N + 1))
    last = N - 1
    for k in range(k1 + 1)[::-1]:
        cnt = 2 ** k
        lst = lst[last + 1 - cnt:last + 1] + lst[:last + 1 - cnt] + lst[last + 1:]
        last = cnt - 1

    last = N - 1
    for k in range(k2 + 1)[::-1]:
        cnt = 2 ** k
        lst = lst[last + 1 - cnt:last + 1] + lst[:last + 1 - cnt] + lst[last + 1:]
        last = cnt - 1

    for i in range(N):
        if target[i] != lst[i]:
            return False
    return True


N = int(input())
target = list(map(int, input().split()))
mxk = 0
while 2 ** (mxk + 1) <= N:
    mxk += 1

print(*solve(mxk))
