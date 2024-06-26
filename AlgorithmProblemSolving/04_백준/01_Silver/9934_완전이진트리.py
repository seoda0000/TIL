'''
완전이진트리
https://www.acmicpc.net/problem/9934
백준 실버1 9934

상근이는 슬로베니아의 도시 Donji Andrijevci를 여행하고 있다.
이 도시의 도로는 깊이가 K인 완전 이진 트리를 이루고 있다. 깊이가 K인 완전 이진 트리는 총 2K-1개의 노드로 이루어져 있다.
각 노드에는 그 곳에 위치한 빌딩의 번호가 붙여져 있다. 또, 가장 마지막 레벨을 제외한 모든 집은 왼쪽 자식과 오른쪽 자식을 갖는다.

상근이는 도시에 있는 모든 빌딩에 들어갔고, 들어간 순서대로 번호를 종이에 적어 놓았다.
한국으로 돌아온 상근이는 도시가 어떻게 생겼는지 그림을 그려보려고 하였으나, 정확하게 기억이 나지 않아 실패했다.
하지만, 어떤 순서로 도시를 방문했는지 기억해냈다.

가장 처음에 상근이는 트리의 루트에 있는 빌딩 앞에 서있다.
현재 빌딩의 왼쪽 자식에 있는 빌딩에 아직 들어가지 않았다면, 왼쪽 자식으로 이동한다.
현재 있는 노드가 왼쪽 자식을 가지고 있지 않거나 왼쪽 자식에 있는 빌딩을 이미 들어갔다면, 현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다.
현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동한다.
현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동한다.

상근이가 종이에 적은 순서가 모두 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램을 작성하시오.
'''

K = int(input())
arr = list(map(int, input().split()))
ans = [arr]
N = 2**K - 1  # arr 길이
for k in range(K-1):
    tmp = []
    n = len(ans[-1])
    for i in range(1, n//2+1): # 홀수 인덱스 -> 윗 레벨 노드 추출
        num = ans[-1].pop(i)
        tmp.append(num)
    ans.append(tmp)
for a in ans[::-1]:
    print(*a)


"""
1년 후 풀이
"""

from collections import defaultdict
def check(s, e, k):
    n = (s+e)//2
    dic[k].append(nums[n])
    if s >= e:
        return

    check(s, n-1, k+1)
    check(n+1, e, k+1)
    return

K = int(input())
nums = list(map(int, input().split()))
dic = defaultdict(list)
check(0, len(nums)-1, 1)

for k in range(1, K+1):
    print(*dic[k])