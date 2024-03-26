def solve(nth):
    if nth == M:
        print(*temp)
        return

    for n in range(N):
        temp[nth] = lst[n]
        solve(nth+1)


N, M = map(int, input().split())
lst = sorted(list(set(map(int, input().split()))))
N = len(lst)
temp = [0] * M
solve(0)
