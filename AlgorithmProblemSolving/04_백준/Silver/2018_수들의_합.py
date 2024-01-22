N = int(input())
ans = 0
s = 1
e = 0
for i in range(1, N+1):
    e = i
    while sum(range(s, e+1)) > N:
        s += 1

    if sum(range(s, e+1)) == N:
        ans += 1

print(ans)