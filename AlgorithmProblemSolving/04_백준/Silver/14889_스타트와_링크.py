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
n = N//2                                      # 한팀 당 인원수
team = list(combinations(ppl, n))             # 두 팀으로 나누는 조합 리스트
team = list(combinations(ppl, n))[:len(team)//2]  # 앞의 절반만 고려
mlst = []                                     # 전력 차이 리스트
for t in team:
    match = 0                             # 첫번째 팀
    member1 = list(combinations(t, 2))        # 팀 멤버 중 두명씩 고르기
    for m in range(len(member1)):
        i, j = member1[m]
        match += arr[i][j] + arr[j][i]        # 전력 계산

    t2 = ppl - set(t)                     # 두번째 팀
    member2 = list(combinations(t2, 2))       # 팀 멤버 중 두명씩 고르기
    for m in range(len(member2)):
        i, j = member2[m]
        match -= (arr[i][j] + arr[j][i])      # 전력 계산
    mlst.append(abs(match))               # 전력 차이 리스트 갱신
print(min(mlst))                          # 최소값 출력

