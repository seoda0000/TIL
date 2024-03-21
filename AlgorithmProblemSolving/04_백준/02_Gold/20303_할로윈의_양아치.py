from collections import deque

import sys

input = sys.stdin.readline


def check_friends(s):
    global all_candy_cnt

    v[s] = 1
    q = deque([s])
    child_cnt = 1
    candy_cnt = candies[s]
    while q:
        cur = q.popleft()

        for nxt in friends[cur]:
            if v[nxt]: continue
            v[nxt] = 1
            q.append(nxt)
            child_cnt += 1
            candy_cnt += candies[nxt]
    if child_cnt < K:
        all_candy_cnt += candy_cnt
        child_candy_lst.append((child_cnt, candy_cnt))
    return


N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))
friends = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

v = [0] * (N + 1)
child_candy_lst = [(0, 0)]
all_candy_cnt = 0
for i in range(1, N + 1):
    if v[i]: continue
    check_friends(i)
ans = 0
C = len(child_candy_lst)
child_candy_lst.sort()

arr = [[0] * K for _ in range(C)]

for c in range(1, C):
    child, candy = child_candy_lst[c]
    for i in range(K):
        if i - child >= 0:
            arr[c][i] = max(arr[c - 1][i - child] + candy, arr[c - 1][i])
        else:
            arr[c][i] = arr[c - 1][i]


print(max(arr[-1]))
