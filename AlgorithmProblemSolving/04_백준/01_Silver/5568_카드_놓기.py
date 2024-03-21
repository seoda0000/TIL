def putCards(nth, st):
    if nth == K:
        ans.append(st)
        return

    for i in range(N):
        if v[i]: continue

        v[i] = 1
        putCards(nth + 1, st + cards[i])
        v[i] = 0




ans = []

N = int(input())
K = int(input())
cards = [input() for _ in range(N)]
v = [0] * N

putCards(0, "")

print(len(set(ans)))
