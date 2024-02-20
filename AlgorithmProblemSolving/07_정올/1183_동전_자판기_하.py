"""
https://jungol.co.kr/problem/1183
정올 골드2 1183

철수는 동전 자판기를 자주 이용한다.

그래서 그는 항상 상당히 많은 개수의 동전들을 주머니에 가지고 다니는데, 동전들이 주머니에서 짤랑거리는 것을 듣기 싫어한다.

그래서 철수는 동전자판기에서 무언가 살 때는 되도록 많은 개수의 동전을 사용한다.

철수의 주위에 있는 자판기들은 아주 구형인 모델이어서 지폐를 사용할 수 없고, 또, 정확한 액수만을 넣어야 한다.


이 문제는 철수가 가지고 있는 동전 중 최대 개수의 동전을 이용하여 자판기의 물건을 구입하는 방법을 출력하는 프로그램을 작성하는 것이다.
"""


def give_coins(nth, remain):
    if remain == 0:
        return True

    if nth < 0:
        return False

    coin = coins[nth]

    if remain % coin:
        return False

    for i in range(min(remain // coin, cnts[nth]), -1, -1):
        ans[nth] = i
        if give_coins(nth - 1, remain - i * coin):
            return True
        ans[nth] = 0

    return False


W = int(input())
coins = [500, 100, 50, 10, 5, 1]
cnts = list(map(int, input().split()))
ans = [0] * 6

give_coins(5, W)
print(sum(ans))
print(*ans)
