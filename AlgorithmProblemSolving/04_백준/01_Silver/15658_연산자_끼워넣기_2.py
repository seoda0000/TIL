def calc(nth, res):
    global mx, mn
    if nth == N - 1:
        mx = max(mx, res)
        mn = min(mn, res)
        return

    for i in range(4):
        if oper_cnts[i] == cnts[i]: continue

        cnts[i] += 1

        num = nums[nth + 1]

        if i == 0:  # 덧셈
            new_res = res + num
        elif i == 1:  # 뺄셈
            new_res = res - num
        elif i == 2:  # 곱셈
            new_res = res * num
        else:  # 나눗셈
            if res < 0:
                new_res = -((-res) // num)
            else:
                new_res = res // num

        calc(nth + 1, new_res)

        cnts[i] -= 1


N = int(input())
nums = list(map(int, input().split()))
oper_cnts = list(map(int, input().split()))
mx = -1_000_000_000
mn = 1_000_000_000
cnts = [0] * 4
calc(0, nums[0])
print(mx)
print(mn)
