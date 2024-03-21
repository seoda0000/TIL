def printNums(nth):
    if nth == N:
        print(*temp)

    for i in range(1, N + 1):
        if v[i]: continue

        v[i] = 1
        temp[nth] = i
        printNums(nth + 1)
        v[i] = 0

    return


N = int(input())

v = [0] * (N + 1)
temp = [0] * (N)

printNums(0)
