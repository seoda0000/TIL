"""
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

"""
T = int(input())

for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    c = [0] * 10  # 카운트 배열

    for i in lst:  # 카운트 조회
        c[i] += 1

    ans = mx = 0
    for j in range(10):
        if c[j] >= mx and j >= ans:  # 카운트가 같고 더 큰 숫자
            ans, mx = j, c[j]
        elif c[j] > mx:  # 카운트가 큰 숫자
            ans, mx = j, c[j]

    print(f"#{case} {ans} {mx}")
