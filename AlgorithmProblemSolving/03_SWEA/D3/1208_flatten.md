## 1208. [S/W 문제해결 기본] 1일차 - Flatten

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&

한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

* 가로 길이는 항상 100으로 주어진다.

* 모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

* 덤프 횟수는 1이상 1000이하로 주어진다.

* 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

```python
for tcase in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    n = len(lst)

    # 최대 dump 횟수만큼 dump하기
    for _ in range(dump):
        lst.sort()
        if lst[-1] - lst[0] <= 1: break  # 빠른 종료조건
        lst[0] += 1
        lst[-1] -= 1

    ans = max(lst) - min(lst)
    print(f"#{tcase} {ans}")
```

* index를 활용할 경우 break 조건을 넣지 않아도 된다.
* index는 언제나 앞에서 찾기 때문에, 최소값과 최대값이 같을 경우 같은 위치를 잡게 된다.

```python
for test_case in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    cnt = 0

    while cnt < N:
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
        cnt += 1
    print(f'#{test_case} {max(lst) - min(lst)}')

```

* 내장함수를 사용하지 않고 Bubble sort를 이용한 풀이도 추가했다.
* 빠른 종료조건을 추가했다.

```python

# 함수 정의
def mysort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


for tcase in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    n = len(lst)

    # 최대 dump 횟수만큼 dump하기
    for _ in range(dump):
        mysort(lst)
        if lst[-1] - lst[0] <= 1: break  # 빠른 종료조건
    lst[0] += 1
    lst[-1] -= 1
mysort(lst)
ans = lst[-1] - lst[0]

print(f"#{tcase} {ans}")
```

* 내장함수를 사용하지 않고 Counting sort를 이용한 풀이도 추가했다.

```python

# 함수 정의
def mysort(lst):
    c = [0] * 101
    temp = [0] * 100

    for i in range(100):
        c[lst[i]] += 1

    for i in range(1, 101):
        c[i] += c[i - 1]

    for j in range(99, -1, -1):
        c[lst[j]] -= 1
        temp[c[lst[j]]] = lst[j]
    return temp


for tcase in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    n = len(lst)

    # 최대 dump 횟수만큼 dump하기
    for _ in range(dump):
        lst = mysort(lst)
        if lst[-1] - lst[0] <= 1: break  # 빠른 종료조건
        lst[0] += 1
        lst[-1] -= 1
    lst = mysort(lst)
    ans = lst[-1] - lst[0]

    print(f"#{tcase} {ans}")
```

* 참고 답안
* sort 하지 않고 min과 max만 찾는다.

```python
def min_max(lst):
    i_min = i_max = 0
    for i in range(1, len(lst)):
        if lst[i_max] < lst[i]:
            i_max = i
        if lst[i_min] > lst[i]:
            i_min = i
    return i_min, i_max


T = 10

for test_case in range(1, T + 1):
    N = 100
    C = int(input())
    lst = list(map(int, input().split()))

    for _ in range(C):  # 이동 회수만큼 반복
        i_min, i_max = min_max(lst)
        if lst[-1] - lst[0] <= 1: break  # 빠른 종료조건
        lst[i_min] += 1
        lst[i_max] -= 1

    i_min, i_max = min_max(lst)
    print(f"#{test_case} {lst[i_max] - lst[i_min]}")

```
