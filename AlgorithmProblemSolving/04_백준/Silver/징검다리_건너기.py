'''
징검다리 건너기
https://www.acmicpc.net/problem/21317
백준 실버2 21317

심마니 영재는 산삼을 찾아다닌다.

산삼을 찾던 영재는 N개의 돌이 일렬로 나열되어 있는 강가를 발견했고, 마지막 돌 틈 사이에 산삼이 있다는 사실을 알게 되었다.

마지막 돌 틈 사이에 있는 산삼을 캐기 위해 영재는 돌과 돌 사이를 점프하면서 이동하며 점프의 종류는 3가지가 있다.

점프의 종류에는 현재 위치에서 다음 돌로 이동하는 작은 점프, 1개의 돌을 건너뛰어 이동하는 큰 점프, 2개의 돌을 건너뛰어 이동하는 매우 큰 점프가 있다.

각 점프를 할 때는 에너지를 소비하는데, 이 때 작은 점프와 큰 점프시 소비되는 에너지는 점프를 하는 돌의 번호마다 다르다.

매우 큰 점프는 단 한 번의 기회가 주어지는데, 이때는 점프를 하는 돌의 번호와 상관없이 k만큼의 에너지를 소비한다.

에너지를 최대한 아껴야 하는 영재가 산삼을 얻기 위해 필요한 에너지의 최솟값을 구하여라.

영재는 첫 번째 돌에서부터 출발한다.

'''
N = int(input())
small = []
big = []
for _ in range(N-1):
    a, b = map(int, input().split())
    small.append(a)
    big.append(b)
k = int(input())

lst = [5000*20] * N
lst[0] = 0
if N == 1:
    ans = 0
elif N == 2:
    ans = small[0]
else:
    lst[1] = small[0]
    lst[2] = big[0]
    for n in range(2, N):
        lst[n] = min(lst[n-1] + small[n-1], lst[n-2] + big[n-2], lst[n])
    ans = lst[-1]
    if N > 3:
        for i in range(N-3):
            if lst[i+3] > lst[i] + k:
                tmp = lst[:]
                tmp[i+3] = tmp[i] + k
                if i+4 < N:
                    for n in range(i+4, N):
                        tmp[n] = min(tmp[n-1] + small[n-1], tmp[n-2] + big[n-2], tmp[n])
                ans = min(ans, tmp[-1])

print(ans)