N = int(input())
k = len(str(N))

for i in range(max(0, N - 10 * k), N):
    sm = i
    for j in range(len(str(i))):
        sm += int(str(i)[j])
    if sm == N:
        print(i)
        break
else:
    print(0)
