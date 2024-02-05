def printNums(nth, lst):
    if nth == M:
        print(*lst)
    for n in range(1, N+1):
        if n not in lst:
            printNums(nth + 1, lst + [n])
    return


N, M = map(int, input().split())
printNums(0, [])
