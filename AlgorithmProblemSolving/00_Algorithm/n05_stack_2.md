- [**계산기1**](#계산기1)
    + [중위표기법에서 후위표기법으로의 변환 알고리즘(스택 이용)](#중위표기법에서-후위표기법으로의-변환-알고리즘(스택-이용))
- [**계산기2**](#계산기2)
    + [후위 표기법의 수식을 계산(스택 이용)](#후위-표기법의-수식을-스택을-이용하여-계산)
- [**백트랙킹 Backtracking**](#백트랙킹-Backtracking)
    + [백트랙킹과 깊이우선탐색과의 차이](#백트랙킹과-깊이우선탐색과의-차이)
    + [백트랙킹 기법](#백트랙킹-기법)
    + [백트랙킹 절차](#백트랙킹-절차)
- [**분할정복 알고리즘**](#분할정복-알고리즘)
    + [설계 전략](#설계-전략)
- [**퀵 정렬**](#퀵-정렬)
    + [정렬 과정](#정렬-과정)
- [**정렬 알고리즘 비교**](#정렬-알고리즘-비교)


---



# 계산기1

문자열 수식 계산의 일반적 방법

1. 중위 표기법의 수식을 후위 표기법으로 변경한다.
2. 후위 표기법의 수식을 스택을 이용하여 계산한다.

중위표기법 : 연산자를 피연산자의 가운데 표기하는 방법 `A+B`

후위표기법 : 연산자를 피연산자 뒤에 표기하는 방법 `AB+`

<br>

### 중위표기법에서 후위표기법으로의 변환 알고리즘(스택 이용)

1. 입력 받은 중위 표기식에서 토큰을 읽기
2. 토큰이 **피연산자**이면 토큰을 **출력**
3. 토큰이 **연산자**일 때
    1. 이 토큰이 스택의 top에 저장되어 있는 연산자보다 **우선순위가 높으면 스택에 push**
    2. 그렇지 않다면 스택 top의 연산자의 우선순위가 **토큰의 우선순위보다 작을 때까지 스택에서 pop**한 후 **토큰의 연산자를 push**
    3. 만약 top에 연산자가 없으면 push
4. 토큰이 오른쪽 괄호 **‘)’**면 스택 top에 왼쪽 괄호 **‘(’가 올 때까지 스택에 pop 연산을 수행**하고 pop한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
5. 중위표기식에 더 읽을 것이 없다면 중지. 있다면 1부터 다시 반복
6. 스택에 남아있는 연산자를 모두 pop하여 출력

⭐스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선순위가 가장 낮다.

| 토큰 | isp (스택 안) | icp (스택 밖) |
| --- | --- | --- |
| ) | - | - |
| *, / | 2 | 2 |
| +, - | 1 | 1 |
| ( | 0 | 3 |

<br>

---

# 계산기2

### 후위 표기법의 수식을 스택을 이용하여 계산

1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산. 연산 결과를 다시 스택에 push
3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

<br>

---

# 백트랙킹 Backtracking

- 해를 찾는 도중에 ‘막히면’ (즉, 해가 아니면) 되돌아가서 다시 해를 찾아가는 기법
- 최적화 문제와 결정 문제(yes/no) 해결 가능

<br>

### 백트랙킹과 깊이우선탐색과의 차이

- 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄임. (가지치기 Prunning)
- 일반적으로 깊이우선탐색보단 경우의 수가 줄어들지만 최악의 경우에는 지수함수 시간을 요함.

<br>

### 백트랙킹 기법

- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 부모 노드로 되돌아감(backtracking).
- 가지치기(prunning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

<br>

### 백트랙킹 절차

- 상태 공간 트리의 깊이 우선 검색을 실시
- 각 노드가 유망한지 점검
- 만약 유망하지 않다면 부모 노드로 돌아가서 검색 계속

<br>

---

# 분할정복 알고리즘

- 유래
    - 나폴레옹. 전력이 우세한 연합군의 중앙부로 쳐들어가 연합군을 둘로 나눔. 한 부분씩 격파.

### 설계 전략

- 분할 Divide : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복 Conquer : 나눈 작은 문제를 각각 해결한다.
- 통합 Combine : 필요하다면 해결된 해답을 모은다.

### 거듭제곱의 예

```python
# Base ^ Exponent
def Power(Base, Exponent):
	if Exponent == 0 or Base == 0:
		return 1

	if Exponent % 2 == 0 :  # 짝수 : C^n = C^(n/2) * C^(n/2)
		NewBase = Power(Base, Exponent/2)
		return NewBase * NewBase

	else:                   # 홀수 : C^n = C^((n-1)/2) * C^((n-1)/2) * C
		NewBase = Power(Base, (Exponent-1)/2)
		return (NewBase * NewBase) * Base
```


<br>


# 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
    - top-down 방식
- 시간 복잡도 O(n log n)


<br>


### 정렬 과정

- 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
- 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합 → 최종 1개

```python
def merge_sort(lst):
    global cnt
    if len(lst)<2:  # 정렬대상이 1개이면 종료
        return lst
 
    m = len(lst)//2 # [1] 반을 나눠서 각각을 정렬
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

 
    # [2] 좌우 더 작은값을 하나씩 추가
    ret = []
    l = r = 0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            ret.append(left[l])
            l+=1
        else:
            ret.append(right[r])
            r+=1
    ret += left[l:]+right[r:]
    return ret
 
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f'#{test_case}', lst)
```

---

# 퀵 정렬

- 주어진 배열을 두개로 분할하고, 각각을 정렬
- 분할할 때 **기준 아이템(pivot item)** 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치
- 합병이라는 후처리 불필요

<br>

### 정렬 과정

- **피봇** : 중앙 원소로 결정
- **L** : 왼쪽 끝에서 오른쪽으로 이동하면서 피봇보다 크거나 작은 원소 찾기
- **R** : 오른쪽 끝에서 왼쪽으로 이동하면서 피봇보다 작은 원소 찾기
- **L과 R이 만났을 때**, **원소를 pivot과 교환**하여 위치 확정
- **L과 R이 만나기 전 둘 다 원소를 찾았다면 원소끼리 교환**

```python
def qsort(lst):
    if len(lst)<2:  # 종료조건: 한 개라면 정렬 진행하지 않음
        return lst
 
    # [1] p(기준)를 기준으로 좌/우로 나눔: 단위작업
    p = lst.pop()
    left = []
    right = []
    for n in lst:
        if n<p:
            left.append(n)
        else:
            right.append(n)
 
    # [2] 왼쪽정렬, 오른쪽정렬, 그 결과를 합쳐서 리턴
    return qsort(left) + [p] + qsort(right)
 

def qsort_idx(s, e):
    if s>=e:    # 정렬해야할 개수가 1개 이하
        return
 
    # [1] P기준으로 작은값(왼쪽), 그외 (오른쪽) : 단위작업
    p, t = e, s
    for i in range(s, e):
        if lst[i]<lst[p]:   # p 왼쪽으로 이동시켜야 함
            lst[i],lst[t] = lst[t],lst[i]
            t+=1
    lst[p],lst[t] = lst[t],lst[p]
    p = t
 
    # [2] p기준 왼쪽정렬, 오른쪽 정렬
    qsort_idx(s, p-1)   # 왼쪽 정렬
    qsort_idx(p+1, e)   # 오른쪽 정렬
 

T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    # lst = qsort(lst)      # 1800ms
    # qsort_idx(0, N-1)     # 1500ms
    lst.sort()                  # 1000ms
    print(f'#{test_case} {lst[N//2]}')
```

---

# 정렬 알고리즘 비교

| 알고리즘 | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고 |
| --- | --- | --- | --- | --- |
| 버블 정렬 | O(n^2) | O(n^2) | 비교와 교환 | 가장 쉬움 |
| 카운팅 정렬 | O(n+k) | O(n+k) | 비교환 방식 | n이 비교적 작을 때만 가능 |
| 선택 정렬 | O(n^2) | O(n^2) | 비교와 교환 | 교환의 회수가 버블, 삽입정렬보다 작다. |
| 퀵 정렬 | O(nlogn) | O(n^2) | 분할 정복 | 평균적으로 가장 빠름 |
| 삽입 정렬 | O(n^2) | O(n^2) | 비교와 교환 | n의 개수가 작을 때 효과적 |
| 병합 정렬 | O(nlogn) | O(nlogn) | 분할 정복 | 연결리스트의 경우 가장 효율적인 방식 |