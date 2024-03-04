import sys

input = sys.stdin.readline


def calc(res):
    global ans
    if res > n:
        return

    if res == n:
        ans += 1
        return

    for i in range(1, 4):
        calc(res + i)
    return


T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    calc(0)
    print(ans)
