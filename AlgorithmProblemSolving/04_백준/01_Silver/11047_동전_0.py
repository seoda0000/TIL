def cal_coin(remain, cnt, last):
    global ans
    if remain == 0:
        return cnt

    for n in range(last)[::-1]:
        coin = coins[n]
        if remain >= coin:
            res = cal_coin(remain % coin, cnt + remain // coin, n)
            if res:
                return res

    return 0


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = cal_coin(K, 0, N)
print(ans)
