'''
창고 다각형
https://www.acmicpc.net/problem/2304
백준 실버2 2304

N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다.
이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.

지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
지붕의 가장자리는 땅에 닿아야 한다.
비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다.
기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.

'''


n = int(input())
lst = [list(map(int, input().split())) for n in range(n)]
lst.sort()
peakh, peak = max([(i[1], i[0]) for i in lst])  # (꼭대기 높이, 꼭대기 좌표)
peakidx = lst.index([peak, peakh])              # 꼭대기 index
ans = peakh                                     # 꼭대기 면적 더하기

tmp = lst[0]                                # 첫 값부터 시작
for i in range(1, peakidx):                 # 꼭대기 왼쪽 건물
    w, h = lst[i]
    if h > tmp[1]:                          # 만약 더 높은 건물이 발견되면
        ans += (w - tmp[0]) * tmp[1]            # 면적 더하기
        tmp = lst[i]                            # 건물 정보 저장
ans += (peak - tmp[0]) * tmp[1]                 # 꼭대기 직전까지 영역 처리

tmp = lst[-1]                               # 마지막 값부터 시작
for i in range(peakidx+1, n-1)[::-1]:       # 꼭대기 오른쪽 건물
    w, h = lst[i]
    if h > tmp[1]:                          # 만약 더 높은 건물이 발견되면
        ans += (tmp[0] - w) * tmp[1]            # 면적 더하기
        tmp = lst[i]                            # 건물 정보 저장
ans += (tmp[0] - peak) * tmp[1]                 # 꼭대기 직전까지 영역 처리
print(ans)