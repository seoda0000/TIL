def fill_nums(nth):
    if nth == M:
        ans.append(' '.join(map(str,temp)))
        return

    for i in range(N):
        temp[nth] = nums[i]
        fill_nums(nth + 1)
    return


N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
nums.sort()
temp = [-1] * M
fill_nums(0)
print(*ans, sep='\n')
