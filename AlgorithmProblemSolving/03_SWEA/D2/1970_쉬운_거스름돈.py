'''
쉬운 거스름돈
SWEA D2 1970
우리나라 화폐 ‘원’은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다.

S마켓에서 사용하는 돈의 종류는 다음과 같다.
50,000 원
10,000 원
5,000 원
1,000 원
500 원
100 원
50 원
10 원

S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.
'''

T = int(input())

for case in range(1, T+1):
    N = int(input())

    # 거스름돈 리스트
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = []
    for i in lst:
        ans.append(N//i) # 줄 수 있는 돈
        N = N % i # 남은 거스름돈
    print(f'#{case}')
    print(*ans)
