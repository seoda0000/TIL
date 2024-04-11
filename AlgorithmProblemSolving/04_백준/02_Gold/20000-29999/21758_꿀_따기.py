'''
꿀 따기
https://www.acmicpc.net/problem/21758
백준 골드5 21758

아래와 같이 좌우로 $N$개의 장소가 있다.

장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다. 또, 다른 한 장소를 골라서 벌통을 둔다.

두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다. 각 장소에 적힌 숫자는 벌이 지나가면서 꿀을 딸 수 있는 양이다.

두 마리가 모두 지나간 장소에서는 두 마리 모두 표시된 양 만큼의 꿀을 딴다. (벌통이 있는 장소에서도 같다.)
벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.

장소들의 꿀 양을 입력으로 받아 벌들이 딸 수 있는 가능한 최대의 꿀의 양을 계산하는 프로그램을 작성하라.
'''


N = int(input())
lst = list(map(int, input().split()))

# 왼쪽 끝에 벌집이 있을 때 (오른쪽 끝에 벌 두 마리가 있을 때)
ans1 = tmp = sum(lst[:N-2]) * 2
for a in range(N-2, 1, -1):
    tmp += lst[a] - lst[a-1]*2
    if tmp > ans1:
        ans1 = tmp


# 오른쪽 끝에 벌집이 있을 때 (왼쪽 끝에 벌 두 마리가 있을 때)
ans2 = tmp = sum(lst[2:N]) * 2
for a in range(1, N-2):
    tmp += lst[a] - lst[a+1]*2
    if tmp > ans2:
        ans2 = tmp


# 중앙에 벌집이 있을 때 (양쪽 끝에 벌 한 마리가 있을 때))
ans3 = sum(lst[1:N-1]) + max(lst[1:N-1])

ans = max(ans1, ans2, ans3)
print(ans)

