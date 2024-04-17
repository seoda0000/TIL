import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    ipts = list(map(int, input().split()))
    contacts = defaultdict(list)
    for n in range(0, N, 2):
        contacts[ipts[n]].append(ipts[n + 1])
    v = [0] * 101
    v[S] = 1
    lst = [S]

    while True:
        nxtLst = []

        for c in lst:
            for nxt in contacts[c]:
                if v[nxt]: continue
                v[nxt] = 1
                nxtLst.append(nxt)
        if nxtLst:
            lst = nxtLst
        else:
            break
    ans = max(lst)

    print(f'#{test_case} {ans}')
