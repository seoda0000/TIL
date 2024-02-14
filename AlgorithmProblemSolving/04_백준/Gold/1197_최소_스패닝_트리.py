def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    p[find(b)] = find(a)
    return


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
p = list(range(V + 1))
ans = 0
for n1, n2, w in edges:
    if find(n1) == find(n2):
        continue
    ans += w
    union(n1, n2)
print(ans)
