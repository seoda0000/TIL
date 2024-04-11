def findFriends(nth, cur):
    global ans

    if nth == 5:
        ans = 1
        return

    for nxt in relations[cur]:
        if v[nxt]: continue
        v[nxt] = 1
        findFriends(nth + 1, nxt)
        v[nxt] = 0
    return


N, M = map(int, input().split())
relations = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)
v = [0] * N
ans = 0

for n in range(N):
    v[n] = 1
    findFriends(1, n)
    v[n] = 0
    if ans: break
print(ans)
