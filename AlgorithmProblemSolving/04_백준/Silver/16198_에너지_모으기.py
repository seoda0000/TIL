def get_energy(lst, energy):
    global ans

    ln = len(lst)
    if ln <= 2:
        ans = max(ans, energy)

    for x in range(1, ln - 1):
        get_energy(lst[:x] + lst[x + 1:], energy + lst[x - 1] * lst[x + 1])

    return


N = int(input())
marbles = list(map(int, input().split()))
ans = 0
get_energy(marbles, 0)
print(ans)
