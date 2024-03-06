'''
스타트와 링크
https://www.acmicpc.net/problem/14889
백준 실버2 14889

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.

'''

from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ppl = set(range(N))
n = N // 2  # 한팀 당 인원수
team = list(combinations(ppl, n))  # 두 팀으로 나누는 조합 리스트
team = list(combinations(ppl, n))[:len(team) // 2]  # 앞의 절반만 고려
mlst = []  # 전력 차이 리스트
for t in team:
    match = 0  # 첫번째 팀
    member1 = list(combinations(t, 2))  # 팀 멤버 중 두명씩 고르기
    for m in range(len(member1)):
        i, j = member1[m]
        match += arr[i][j] + arr[j][i]  # 전력 계산

    t2 = ppl - set(t)  # 두번째 팀
    member2 = list(combinations(t2, 2))  # 팀 멤버 중 두명씩 고르기
    for m in range(len(member2)):
        i, j = member2[m]
        match -= (arr[i][j] + arr[j][i])  # 전력 계산
    mlst.append(abs(match))  # 전력 차이 리스트 갱신
print(min(mlst))  # 최소값 출력

"""
1년 후 풀이
"""

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
