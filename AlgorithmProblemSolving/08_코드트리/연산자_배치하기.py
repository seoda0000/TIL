def make_idx(nth):
    if nth >= M:
        calc()
        return
    for n in range(M):
        if n in idx:
            continue
        idx[nth] = n
        make_idx(nth + 1)
        idx[nth] = -1


def calc():
    global mx, mn

    num = nums[0]

    for n in range(M):
        if operator[idx[n]] == '+':
            num += nums[n + 1]
        elif operator[idx[n]] == '-':
            num -= nums[n + 1]
        else:
            num *= nums[n + 1]


    mx = max(num, mx)
    mn = min(num, mn)


N = int(input())
nums = list(map(int, input().split()))
cnts = list(map(int, input().split()))
operator = '+' * cnts[0] + '-' * cnts[1] + '*' * cnts[2]
M = sum(cnts)
idx = [-1] * M
mx = -1_000_000_000
mn = 1_000_000_000
make_idx(0)
print(mn, mx)
