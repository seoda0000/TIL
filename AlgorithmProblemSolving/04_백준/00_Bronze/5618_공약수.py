N = int(input())
num = list(map(int, input().split()))
ans = []

a, b = num[0], num[1]
while b % a != 0:
    a, b = b % a, a
if N > 2:
    b = num[2]
    while b % a != 0:
        a, b = b % a, a


for i in range(1, a+1):
    for j in range(N):
        if num[j] % i != 0:
            break
    else:
        ans.append(i)
for a in ans:
    print(a)
