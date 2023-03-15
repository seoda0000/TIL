# 실패

import sys
input = sys.stdin.readline
N = int(input())
weights = list(map(int, input().split()))
M = int(input())
questions = list(map(int, input().split()))
answer = []
for m in range(M):
    tw = questions[m]
    cw = 0
    i = 0
    ans = "N"

    while i < N and ans == "N":

        for n in range(i, N):
            cw += weights[n]
            if tw == cw:
                ans = "Y"
                break
            elif tw < cw:

                tw += weights[i]
                cw = 0
                i += 1
                break
        else:
            break
    answer.append(ans)

print(*answer)

