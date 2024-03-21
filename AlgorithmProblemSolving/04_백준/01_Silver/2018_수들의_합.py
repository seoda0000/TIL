N = int(input())
ans = 0
s = e = 1
temp = 1
while e <= N:
    if temp == N:
        ans += 1
    e += 1
    temp += e

    while temp > N:
        temp -= s
        s += 1

print(ans)