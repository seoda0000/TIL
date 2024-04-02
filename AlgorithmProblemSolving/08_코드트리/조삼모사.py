"""
실행시간: 364 -> 416
풀이시간: 118분 -> 13분

실행시간은 늘어났지만 코드길이는 짧아졌다. (한 배열을 계속 쓰는 것이 함수로 넘기는 것보다 빠르다)
계산 함수를 조금 더 작은 단위에 적용하여 가독성을 높였다.
가장 괴로운 문제였는데 순열 조합만 실수하지 않으면 간단하다.
너무 복잡하게 생각하지 말고 실수를 점검하자

"""

"""
17:23 시작
17:28 구상 완료
17:36 코드 점검 및 제출
"""


def pick(cnt, lst, si):
    global ans
    if cnt == N // 2:
        a = calc(lst)
        b = calc(list(ST - set(lst)))
        ans = min(ans, abs(a - b))
        return

    for i in range(si, N):
        pick(cnt + 1, lst + [i], i + 1)
    return


def calc(lst):
    nl = len(lst)
    p = 0

    for a in range(nl - 1):
        for b in range(a + 1, nl):
            p += P[lst[a]][lst[b]] + P[lst[b]][lst[a]]

    return p


N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
ST = set(range(N))
ans = N * N * 100 + 1
pick(1, [0], 1)
print(ans)

"""
15:18 2차 구현 실패 후 버림
16:06 다른 문제 풀고 돌아옴

처음엔 단순히 모든 조합을 구하고 값을 도출하는 로직으로 짰다. 단순하고 다른 방법이 없어보여서 구상을 대충하고 구현에 들어갔다.
특히 N개 중 N//2개 뽑기 <- 정도만 쓰고 들어간 게 문제이지 않을까... 조합으로 풀어야 하는데 순열로 풀었다.

시간초과가 난 후에는 일의 강도를 계산하는 로직이 문제라고 판단했고 그 부분을 최적화하려고 노력했다. (결론적으로 무의미한 노력...)
문제와 코드를 엄청나게 찬찬히 살펴보았는데도 순열 조합 실수 부분을 인지하지 못했다!
아마 다른 분들이 구현한대로 append pop 방식을 사용해보고자 해서, 기존에 짜던 방식과 다른 방식이라 더더욱 찾지 못한 것 같다.

교훈 : 익숙한 방법을 쓰자

다 지우고 익숙한 방법을 쓰면 풀었을 것 같다...

이후 다른 방향으로 최적화를 고민했고, 모든 조합을 구하기보다 '작업 0과 함께 할 일 뽑기'라는 방법을 구상할 수 있었다. (이 부분은 이후에 응용 가능할 듯)
그러나 역시 순열 조합 부분을 고치지 않아서 시간이 매우 오래 걸렸다.
또한 시간복잡도를 계산할 때도 순열식을 사용하고 지레짐작으로 '완전탐색은 시간 복잡도 때문에 불가능하다'는 판단을 내렸다. 더더욱 신기한 방향으로 문제를 고민했다...

순열 조합을 이전에 실수한 적 있어서... 이런 일이 생긴 건 매우 당연하게 여겨진다.
앞으로는 순열 조합이 나왔을 때 특히 주의해야겠다.
무엇보다 너무 어렵게 생각하지 않아야 한다. 스스로의 구상 실력을 좀 더 믿고 구현 실력을 좀 더 의심하자
"""


def get_combination(morning):
    if len(morning) == N // 2:
        calc()
        return

    for i in range(morning[-1] + 1, N):
        if i in morning:
            continue
        morning.append(i)
        get_combination(morning)
        morning.pop()


def calc():
    global ans
    cnt_morning, cnt_dinner = 0, 0
    for a in range(N // 2 - 1):
        for b in range(a + 1, N // 2):
            idx1 = morning[a]
            idx2 = morning[b]
            cnt_morning += arr[idx1][idx2] + arr[idx2][idx1]

    dinner = list(st - set(morning))
    for a in range(N // 2 - 1):
        for b in range(a + 1, N // 2):
            idx1 = dinner[a]
            idx2 = dinner[b]
            cnt_dinner += arr[idx1][idx2] + arr[idx2][idx1]

    ans = min(ans, abs(cnt_morning - cnt_dinner))

    return


N = int(input())
st = set(range(N))
arr = [list(map(int, input().split())) for _ in range(N)]
morning = [0]  # 아침에 0을 박아두고 시작
ans = 20 * 20 * 100 + 1
get_combination(morning)
print(ans)
