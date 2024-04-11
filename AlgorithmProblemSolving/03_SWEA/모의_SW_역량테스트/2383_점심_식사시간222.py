import sys

sys.stdin = open("input.txt", "r")

from collections import deque


def solve(nth, choices):
    global ans
    if nth == P:
        ans = min(ans, simulate(choices))
        return
    solve(nth + 1, choices)
    choices[nth] = 1
    solve(nth + 1, choices)
    choices[nth] = 0
    return


def simulate(choices):
    arrival_arr = [list(), list()]

    for p in range(P):
        st = choices[p]
        pi, pj = ppl_lst[p]
        si, sj = stair_lst[st]
        arrival_arr[st].append(abs(pi - si) + abs(pj - sj))

    time_lst = []
    for i in range(2):
        arrival_lst = arrival_arr[i]
        K = k_lst[i]
        stairs = deque()  # 진입 시점

        arrival_lst.sort()
        for arrival in arrival_lst:
            while stairs and stairs[0] + K <= arrival + 1:  # 내려갈 시점까지 계단 비우기
                stairs.popleft()
            if len(stairs) < 3:  # 그냥 진입하기
                stairs.append(arrival + 1)
            else:  # 대기 필요
                t = stairs[0] + K - arrival - 1  # 기다려야 하는 시간
                stairs.popleft()
                stairs.append(arrival + 1 + t)
        if stairs:
            time_lst.append(stairs[-1] + K)

    return max(time_lst)


INF = 21e8
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ppl_lst = []
    stair_lst = []
    k_lst = []
    for i in range(N):
        ipts = list(map(int, input().split()))
        for j in range(N):
            if ipts[j] == 1:
                ppl_lst.append((i, j))
            elif ipts[j]:
                stair_lst.append((i, j))
                k_lst.append(ipts[j])
    P = len(ppl_lst)
    choices = [0] * P
    ans = INF
    solve(0, choices)
    print(f'#{test_case} {ans}')
