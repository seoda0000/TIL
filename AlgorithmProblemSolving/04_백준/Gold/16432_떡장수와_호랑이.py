import sys

input = sys.stdin.readline


def give(nth):
    global flag

    if not flag:
        return False

    if nth == N + 1:
        return True

    tn = len(cakes[nth])

    if tn == 1:
        t = cakes[nth][0]
        if t == ans[nth - 1]: return False
        ans[nth] = t
        if give(nth + 1):
            return True
        else:
            flag = False
            return False

    else:
        for n in range(tn):
            t = cakes[nth][n]

            if t == ans[nth - 1]: continue

            ans[nth] = t

            if give(nth + 1):
                return True
            if not flag:
                return False

    return False


N = int(input())
ans = [0] * (N + 1)
cakes = [[]]
flag = True
for n in range(N):
    ipt = list(map(int, input().split()))
    cakes.append(list(set(ipt[1:])))
res = give(1)
if res:
    print(*ans[1:], sep = '\n')
else:
    print(-1)
