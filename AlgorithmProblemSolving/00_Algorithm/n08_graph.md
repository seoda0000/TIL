- [**그래프**](#그래프)
    + [그래프 유형](#그래프-유형)
    + [인접 Adjacency](#인접-Adjacency)
    + [그래프 경로](#그래프-경로)
    + [그래프 표현](#그래프-표현)
    + [그래프 순회](#그래프-순회)
- [**서로소 집합 Disjoint-sets**](#서로소-집합-Disjoint-sets)
- [**최소 신장 트리(MST)**](#최소-신장-트리(MST))
  * [Prim 알고리즘](#Prim-알고리즘)
  * [Kruskal 알고리즘](#Kruskal-알고리즘)
- [**최단 경로**](#최단-경로)
  * [Dijkstra 알고리즘](#Dijkstra-알고리즘)

---


# 그래프

- 요소들과 이들 사이의 연결 관계를 표현
- 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료구조
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현할 때 용이

### 그래프 유형

- 무향 그래프 Undirected Graph
- 유향 그래프 Directed Graph
- 가중치 그래프 Weighted Graph
- 사이클 없는 방향 그래프 DAG, Directed Acyclic Graph

- 완전 그래프 : 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프 : 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

### 인접 Adjacency

- 두 개의 정점에 간선이 존재하면 서로 인접해 있다고 한다.
- 완전 그래프에 속한 임의의 두 정점들은 모두 인접해 있다.

### 그래프 경로

- 간선들을 순서대로 나열한 것
- 단순경로 : 경로 중 한 정점을 최대 한번만 지나는 경로
- 사이클 Cycle : 시작한 정점에서 끝나는 경로

### 그래프 표현

- 인접 행렬 Adjacent matrix
    - |V|*|V| 2차원 배열
    - 행, 열 번호는 그래프의 정점에 대응
    - 무향 그래프
        - i번째 행의 합 = i번째 열의 합 = Vi의 차수
    - 유향 그래프
        - i번째 행의 합 = Vi의 진출 차수
        - i번째 열의 합 = Vi의 진입 차수
- 인접 리스트 Adjacent List
    - 각 정점마다 해당 정점으로 나가는 간선의 정보 저장
- 간선의 배열
    - 간선(s, e)을 배열에 연속적으로 저장

```python
'''
6 8
0 1 0 2 0 5 0 6 5 3 4 3 5 4 6 4
'''
V, E = map(int, input().split()) # 정점 수-1, 간선 수
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
```

### 그래프 순회

- 비선형구조인 그래프로 표현된 모든 정점을 빠짐없이 탐색하는 것을 의미
- 방법
    - 깊이 우선 탐색 (stack/재귀 이용)
    - 너비 우선 탐색 (queue 이용)

---

# 서로소 집합 Disjoint-sets

- 상호배타집합. 서로 중복 포함된 원소가 없는 집합. 교집합이 없다.
- **대표자** : 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다.

```python
def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

rep = [i for i in range(V+1)]       # 대표원소 배열
```

---

# 최소 신장 트리(MST)

- Minimum Spanning Tree
- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장 트리

<br>

## Prim 알고리즘

- MST 포함되지 않은 노드 중 MST에 연결될 수 있는 최소 비용 노드 선택
- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
    1. 임의 정점을 하나 선택해서 시작
    2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
    3. 모든 정점이 선택될 때까지 1, 2 과정을 반복
- 서로소인 2개의 집합 정보를 유지
    - 트리 정점들 : MST를 만들기 위해 선택된 정점들
    - 비트리 정점들 : 선택되지 않은 정점들

```python
def prim1(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0          # 시작정점의 key
    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i]==0 and key[i]< minV:
                u = i
                minV = key[i]
        MST[u] = 1                  # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])     # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)         # MST 가중치의 합

def prim2(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if MST[i]==1:
                for j in range(V+1):
                    if adjM[i][j]>0 and MST[j]==0 and minV >adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s
```

<br>

## Kruskal 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
    1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
    2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
        - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
    3. n-1개의 간선이 선택될 때까지 2 반복

```python
def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())    # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, v, u])
edge.sort()
rep = [i for i in range(V+1)]       # 대표원소 배열
# MST의 간선수 = 정점 수 - 1
N = V + 1   # 정점 수
cnt = 0     # 선택한 edge의 수
total = 0   # MST 가중치의 합
for w, v, u in edge:
    if find_set(v) != find_set(u):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:  # MST 구성이 끝나면
            break
print(total)
```

---

# 최단 경로

- 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단 경로
    - 다익스트라(dijkstra) 알고리즘 : 음의 가중치 허용 X
    - 벨만-포드(Bellman-Ford) 알고리즘 : 음의 가중치 허용 O
- 모든 정점들에 대한 최단 경로
    - 플로이드-워샬(Floyd-Watshall) 알고리즘

<br>

## Dijkstra 알고리즘

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
- 시작정점에서 끝정점까지의 최단경로에 정점 x가 존재
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사

```python
def dijkstra(s, V):
    U = [0]*(V+1)       # 비용이 결정된 정점을 표시
    U[s] = 1            # 출발점 비용 결정
    for i in range(V+1):
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):      # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점w 중에서
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1                # 비용 결정
        for v in range(V+1):
            if 0< adjM[w][v]< INF:
                D[v] = min(D[v], D[w]+adjM[w][v])

INF = 10000
V, E = map(int, input().split())
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w

D = [0]*(V+1)
dijkstra(0, V)
print(D)

def dijkstra(s, V):
    U = [0]*(V+1)       # 비용이 결정된 정점을 표시
    U[s] = 1            # 출발점 비용 결정
    D[s] = 0
    for v, w in adjL[s]:
        D[v] = w

    # 남은 정점의 비용 결정
    for _ in range(V):      # 남은 정점 개수만큼 반복
        # D[t]가 최소인 t 결정, 비용이 결정되지 않은 정점t 중에서
        minV = INF
        t = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        U[t] = 1                # 비용 결정
        for v, w in adjL[t]:
                D[v] = min(D[v], D[t]+w)

INF = 10000
V, E = map(int, input().split())
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjL[u].append([v, w])

D = [INF]*(V+1)
dijkstra(0, V)
print(D)
```