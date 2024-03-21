def makeNums(nth):
    global ans
    if nth == N:
        result = 0
        for i in range(0, N-1):
            result += abs(temp[i] - temp[i + 1])
        ans = max(ans, result)
        return

    for i in range(N):
        if v[i]: continue
        v[i] = 1
        temp[nth] = nums[i]
        makeNums(nth + 1)
        v[i] = 0



N = int(input())
nums = list(map(int, input().split()))
ans = 0
v = [0] * N
temp = [0] * N
makeNums(0)
print(ans)
