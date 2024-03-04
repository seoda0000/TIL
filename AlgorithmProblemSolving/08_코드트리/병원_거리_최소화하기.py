"""
15:01~15:18 구상+구현+tc 체크 완료
15:18~15:25 1차 리펙토링

브루트포스 말고는 해결 방법이 떠오르지 않았다. 결국 시간복잡도를 따진 후 브루트포스로 구현했다.

중요!
aCb(a개 중 b개 조합 뽑기)의 시간 복잡도: O(2^a)
aPb(a개 중 b개 순열 뽑기)의 시간 복잡도: O(a!)

처음에 조합이 아닌 순열로 안일하게 구현했는데, 제출 전에 시간초과가 걱정되어서 조합으로 수정했다.
여기서 살짝 당황했다. 조합 뽑는 방법이 아무리 쉬워도 종이에 한번 적어보고 가자.

테스트케이스와 검토까지 했다. 조금 느려도 확실하게 가는 습관을 들여야 한다.

"""


def choose_hospital(nth, temp):
    if nth == m + 1:
        check_shortcut(temp[1:])
        return

    for h in range(temp[nth - 1] + 1, Nh):
        temp[nth] = h
        choose_hospital(nth + 1, temp)
        temp[nth] = -1


def check_shortcut(temp):
    global ans

    res = 0
    for c in range(Nc):
        mn = INF

        for idx in temp:
            mn = min(mn, v[c][idx])
        res += mn

    ans = min(ans, res)
    return


N, m = map(int, input().split())
customers = []
hospitals = []
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(N):
        if ipt[j] == 1:
            customers.append((i, j))
        elif ipt[j] == 2:
            hospitals.append((i, j))

Nc = len(customers)
Nh = len(hospitals)
v = [[0] * Nh for _ in range(Nc)]

for c in range(Nc):
    ci, cj = customers[c]
    for h in range(Nh):
        hi, hj = hospitals[h]
        v[c][h] = abs(ci - hi) + abs(cj - hj)

temp = [-1] * (m + 1)
INF = N * N * Nc
ans = INF
choose_hospital(1, temp)
print(ans)
