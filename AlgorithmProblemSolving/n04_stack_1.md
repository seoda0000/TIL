- [**스택 stack**](#스택-stack)
  * [스택의 구현](#스택의-구현)
    + [스택의 push 알고리즘](#스택의-push-알고리즘)
    + [스택의 pop 알고리즘](#스택의-pop-알고리즘)
    + [스택 구현 고려사항](#스택-구현-고려사항---1차원-배열을-사용하여-손쉽게-구현-가능---but-스택의-크기를-변경하기-어렵다.)
  * [스택의 응용 : Function call](#스택의-응용-:-Function-call)
- [**재귀호출**](#재귀호출)
- [**Memoization**](#Memoization)
- [**DP (Dynamic Programming)**](#DP-(Dynamic-Programming))
- [**DFS (깊이우선탐색)**](#DFS-(깊이우선탐색))

---


# 스택 stack

- **물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조**
- 스택에 저장된 자료는 **선형 구조**(자료 간 1대1 관계)를 갖는다.
- 스택에 자료를 삽입하거나 꺼낼 수 있다.
- **후입선출(Last-In-First-Out)** : 마지막에 삽입한 자료를 가장 먼저 꺼냄

## 스택의 구현

- 자료구조 : 자료를 선형으로 저장할 저장소
    - 배열 가능
    - 마지막 삽입된 원소의 위치 : top


| 연산 | 내용 |
| --- | --- |
| push | 삽입. 저장소에 자료를 저장. |
| pop | 삭제. 저장소에서 자료를 꺼냄. |
| isEmpty | 스택이 공백인지 아닌지 확인. |
| peek | 스택의 top에 있는 item 반환 |

<br>

### 스택의 push 알고리즘

```python
# 1. append 메서드 이용
def push(item):
    s.append(item)

# 2. top 이용-1 함수
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1        # 초기값

push(10, size)

# 3. top 이용-2 그냥
top += 1        # push(20)
stack[top] = 20 #
```

### 스택의 pop 알고리즘

```python
# 1. pop 메서드 이용
def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop(-1)

# 2. top 이용-1 함수
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]

print(pop())

# 2. top 이용-2 그냥
if top > -1:
    top -= 1
    print(stack[top])
```

### 스택 구현 고려사항
- 1차원 배열을 사용하여 손쉽게 구현 가능
- but 스택의 크기를 변경하기 어렵다.
  - → 스택의 동적 구현으로 해결 가능

<br>

## 스택의 응용 : Function call

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
- 작업영역 : **시스템 스택**
    - **스택 프레임** : 함수 수행에 필요한 지역변수, 매개변수, 수행 후 복귀할 주소 등 함수 영역
    - 함수 호출 : 스택 프레임 push
    - 함수 완료 : 스택 프레임 pop
- 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

<br>

---

# 재귀호출

- 자기 자신을 호출하여 순환 수행되는 것
- 마지막에 구한 하위 값을 이용하여 상위 값을 구하는 작업을 반복
- ⭐ 재귀호출이라도 다른 메모리공간을 사용한다. f(n) 영역을 스택에 계속 쌓는다.
- 문제점 : 엄청난 중복호출이 존재한다

# Memoization

- **메모리에 넣기. 기억되어야 할 것.** (memorization이 아님!!)
- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법의 핵심이 되는 기술
- `global` 이용

<br>

---

# DP (Dynamic Programming)

- 동적 계획 알고리즘
- 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

<br>

---

# DFS (깊이우선탐색)

- 비선형구조인 그래프구조의 모든 자료를 빠짐없이 검색하는 방법 중 하나.
- **후입선출구조의 스택 사용** : 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로

1. **시작 정점 v**를 결정하여 방문
2. v에 인접한 정점 중
    1. **방문하지 않은 정점 w**가 있으면, 정점 v를 **스택에 push**하고 정점 w 방문. 이후 w를 v로 하여 2 반복
    2. **방문하지 않은 정점이 없으면**, 탐색의 방향을 바꾸기 위해 **스택을 pop**하여 가장 마지막 방문 정점을 v로 하여 2 반복
3. 스택이 공백이 될 때까지 2 반복

```python
# 인접 정점 리스트
adjList = [[1, 2],     # 0
		   [0, 3, 4],  # 1
		   [0, 4],     # 2
		   [1, 5],     # 3
		   [1, 2, 5],  # 4
		   [3, 4, 6],  # 5
		   [5]]        # 6

def dfs(v, N):
	visited = [0] * N
	stack = [0] * N
	top = -1

	visited[v] = 1     # 시작점 방문 표시
	while True:
		for w in adjList[v]:    # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
			if visited[w] == 0:
				top += 1            # push(v)
				stack[top] = v
				v = w               # v <- w (w에 방문)
				visited[w] = 1      # visited[w] <- true
				break
			else:
				if top != -1:
					v = stack[top]    # pop
					top -= 1
				else:                 # 스택이 비어있으면
					break

def dfs(v):
	print(v)    # v 방문
	visited[v] = 1
	for w in adjList[v]:
		if visited[w] == 0:    # 방문하지 않은 w
			dfs(w)
```