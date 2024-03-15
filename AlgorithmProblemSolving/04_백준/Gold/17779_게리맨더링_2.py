'''
0:00~0:06 문제 읽기 -> 뾰족한 방법이 떠오르지 않아서 다른 문제로
1:37~1:38: 문제 다시 시작 및 입력 받기
1:38~1:53 구상
1:53~2:18 1차 구현
2:18~2:30 tc 입력 및 디버깅
2:30~2:42 코드 검토 및 제출

효율적인 방법이 떠오르지 않아서 그냥 그대로 구현했다.
범위 설정하는 게 살짝 까다로웠지만 부등식을 풀어서 어떻게든 했다...
v 배열로도 풀어봐야겠다
'''


def calc(x, y, d1, d2):
    # 1번 선거구
    p1 = 0
    for i in range(x):
        p1 += sum(arr[i][:y + 1])
    for i in range(x, x + d1):
        p1 += sum(arr[i][:y - (i - x)])

    # 2번 선거구
    p2 = 0
    for i in range(x + 1):
        p2 += sum(arr[i][y + 1:])
    for i in range(x + 1, x + d2 + 1):
        p2 += sum(arr[i][y + 2 + (i - (x + 1)):])

    # 3번 선거구
    p3 = 0
    for i in range(x + d1, x + d1 + d2 + 1):
        p3 += sum(arr[i][:y - d1 + (i - (x + d1))])
    for i in range(x + d1 + d2 + 1, N):
        p3 += sum(arr[i][:y - d1 + d2])

    # 4번 선거구
    p4 = 0
    for i in range(x + d2 + 1, x + d1 + d2 + 1):
        p4 += sum(arr[i][y + d2 - (i - (x + d2 + 1)):])
    for i in range(x + d1 + d2 + 1, N):
        p4 += sum(arr[i][y - d1 + d2:])

    # 5번 선거구
    p5 = SM - p1 - p2 - p3 - p4

    return [p1, p2, p3, p4, p5]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
SM = sum([sum(a) for a in arr])
ans = 100 * N * N + 1
for x in range(N - 2):
    for y in range(1, N):
        for d1 in range(1, min(N - x, y + 1)):
            for d2 in range(max(1, d1 - y), min(N - x - d1, N - y)):
                plst = calc(x, y, d1, d2)
                res = max(plst) - min(plst)
                ans = min(ans, res)

print(ans)
