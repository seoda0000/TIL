'''
한윤정이 이탈리아에 가서 아이스크림을 사먹는데
https://www.acmicpc.net/problem/2422
백준 실버4 2422

한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다.
아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다.
어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다. 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다.
이때, 선택하는 방법이 몇 가지인지 구하려고 한다.
'''


from collections import defaultdict
import sys
def input():
    return sys.stdin.readline().rstrip()


def dfs(nth, clst):
    global ans
    if nth == 3:    # 종료 조건
        ans += 1
        return
    for c in card:  # 아직 방문 안했고 뽑은 메뉴 보다 큰 수 일 때 (조합이므로 중복 방지)
        if v[c] == False and (nth == 0 or c > clst[-1]):
            for n in clst:
                if c in bandic[n]:    # 같이 먹으면 안되는 리스트 점검
                    break
            else:
                v[c] = True           # 표시
                dfs(nth+1, clst+[c])  # 다음 메뉴로
                v[c] = False          # clear





N, M = map(int, input().split())
bandic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    bandic[a].append(b)  # 같이 먹으면 안되는 리스트 update
    bandic[b].append(a)

card = list(range(1, N+1))
v = [False] * (N+1)
ans = 0
dfs(0, [])               # 0번째에서 시작
print(ans)
