N = int(input())
a, b = map(int, input().split())
M = int(input())
families = [list() for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    families[x].append(y)
    families[y].append(x)
ans = t = flag = -1

q = [a]
v = [0] * (N + 1)
v[a] = 1

while q:
    n = len(q)
    t += 1

    for _ in range(n):
        now = q.pop(0)

        if now == b:
            ans = t
            flag = 1
            break

        for f in families[now]:
            if v[f] == 0:
                v[f] = 1
                q.append(f)
print(ans)
