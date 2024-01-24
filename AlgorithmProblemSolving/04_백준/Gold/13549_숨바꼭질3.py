"""
시간초과 코드
"""
N, K = map(int, input().split())
v = [0]*200000
ans = 0
t = 0
startLst = [N]
v[N] = 1
mx = K
while True:
    S = len(startLst)
    for z in range(S):
        temp = startLst[z]
        while temp < K:
            if v[temp*2] == 0:
                v[temp*2] = 1
                if temp > K:
                    if mx > K and temp > mx:
                        break
                    elif temp > mx:
                        mx = temp
                startLst.append(temp*2)
                temp = temp*2
            else:
                break

    if K in startLst:
        print(t)
        break

    zeroLst = set(startLst)
    oneLst = list()
    for z in zeroLst:
        if z-1 > 0 and v[z-1] == 0:
            v[z-1] = 1
            oneLst.append(z-1)
        if z+1 <= 100000 and v[z+1] == 0:
            v[z+1] = 1
            oneLst.append(z+1)

    if K in oneLst:
        print(t+1)
        break
    else:
        t += 1
        startLst = list(set(oneLst))


"""
bfs
"""

N, K = map(int, input().split())
v = [-1] * 200001
q = [N]
v[N] = 0

while q:
    now = q.pop(0)

    if now == K:
        print(v[now])
        break

    if now * 2 <= 200000 and v[now * 2] == -1:
        v[now * 2] = v[now]
        q.insert(0, now * 2)

    if 0 <= now - 1 and v[now - 1] == -1:
        v[now - 1] = v[now] + 1
        q.append(now - 1)

    if now + 1 <= 200000 and v[now + 1] == -1:
        v[now + 1] = v[now] + 1
        q.append(now + 1)


