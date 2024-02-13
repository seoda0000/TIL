def makeNum(nth):
    global ans

    if nth == N:
        num = 0
        for n in range(N):
            num += numLst[temp[n]] * 10 ** (N - 1 - n)
        if ans > num > goal:
            ans = num
        return

    for n in range(N):

        if n in temp: continue
        temp[nth] = n
        makeNum(nth + 1)
        temp[nth] = - 1

    return


ipt = input()
N = len(ipt)
goal = int(ipt)
numLst = list(map(int, ipt))
temp = [-1] * N
ans = 1000000
makeNum(0)
if ans == 1000000:
    ans = 0
print(ans)