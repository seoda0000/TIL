"""
https://www.acmicpc.net/problem/1038

백준 골드5 1038 감소하는 수

음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오.
0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

"""
N = int(input())

if N < 10:
    print(N)
elif N > 1022:
    print(-1)
else:
    arr = [[0] * 10] + [[1] * 10] + [[0] * 10 for _ in range(9)]
    cnt = 9
    nth = 2  # 자릿수
    p = 1  # 현재 숫자
    ans = []
    while cnt < N:
        arr[nth][p] = arr[nth][p - 1] + arr[nth - 1][p - 1]
        cnt += arr[nth][p]
        p += 1
        if p == 10:
            nth += 1
            p = nth - 1
    else:
        if p == nth - 1:
            nth -= 1
            p = 10
        ans.append(str(p - 1))

        nth -= 1
        p -= 2

        while nth:
            if cnt - arr[nth][p] < N:
                ans.append(str(p))
                nth -= 1
                p -= 1
                continue
            else:
                cnt -= arr[nth][p]
                p -= 1
        print("".join(ans))
