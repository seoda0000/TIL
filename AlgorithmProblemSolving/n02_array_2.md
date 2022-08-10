- [**2차원 배열**](#2차원-배열)
    + [2차원 배열의 선언](#2차원-배열의-선언)
    + [배열 순회](#배열-순회)
- [**부분집한 생성**](#부분집한-생성)
    + [부분집합의 수](#부분집합의-수)
    + [비트 연산자](#비트-연산자)
- [**검색**](#검색)
  * [순차 검색 sequential search](#순차-검색-sequential-search)
  * [이진 탐색 Binary Search](#이진-탐색-Binary-Search)

- [**인덱스**](#인덱스)
- [**선택 정렬 Selection Sort**](#선택-정렬-Selection-Sort)

---

# 2차원 배열

- 1차원 리스트를 묶어놓은 리스트
- 2차원 리스트의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

<br>

### 2차원 배열의 선언

arr = \[[0, 1, 2, 3], [4, 5, 6, 7]]


| 0 | 1 | 2 | 3 |
| 4 | 5 | 6 | 7 |

```python
'''
3
1 2 3
4 5 6
7 8 9
'''
arr = [list(map(int, input().split())) for _ in range(N)]

'''
3
123
456
789
'''
arr = [list(map(int, input())) for _ in range(N)]
```
<br>

### 배열 순회

- n x m 배열의 n*m개의 원소를 빠짐없이 조사하는 방법
- 행 우선 순회
    
    ```python
    # i 행의 좌표
    # j 열의 좌표
    
    # n = len(arr) 행의 개수
    # m = len(arr[0]) 열의 개수
    
    for i in range(n):
    	for j in range(m):
    		Array[i][j]  # 필요한 연산 수행
    ```
    
- 열 우선 순회
    
    ```python
    # i 행의 좌표
    # j 열의 좌표
    
    for j in range(m):
    	for i in range(n):
    		Array[i][j]  # 필요한 연산 수행
    ```
    
- 지그재그 순회
    
    ```python
    # i 행의 좌표
    # j 열의 좌표
    for i in range(n):
    	for j in range(m):
    		Array[i][j + (m-1-2*j) * (i%2)]  # 필요한 연산 수행
    ```
    

- 델타를 이용한 2차 배열 탐색
    - 2차 배열의 한 좌표에서 4방향의 인접 요소를 탐색하는 방법
    
    ```python
    arr[0...N-1][0...N-1] # NxN 배열
    di[] <- [0, 0, -1, 1] # 상하좌우 
    dj[] <- [-1, 1, 0, 0]
    for i : 1 -> N-1
    		for j : 1 -> N-1
    				for k in range(4) :
    						ni <- i + di[k]
    						nj <- j + dj[k]
    						if 0<=ni<N and 0<=nj<N  # 유효한 인덱스면
    								test(arr[ni][nj])
    	
    
    for i in range(N):
    		for j in range(M):
    				for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    						ni, nj = i+di, j+dj
    						if 0 <= ni < N and 0<=nj<m:
    								print(ni, nj)
    		
    ```
    

- 전치 행렬
    
    ```python
    # i : 행의 좌표 len(arr)
    # j : 열의 좌표 len(arr[0])
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3*3 행렬
    
    for i in range(3) :
    		for j in range(3):
    				if i < j :
    						arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```
    

---

# 부분집한 생성

### 부분집합의 수

- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개

<br>

### 비트 연산자

- << 연산자
    - `1<<n` : 2^n
- & 연산자
    - `i & (1<<j)` : i의 j번째 비트가 1인지 아닌지를 검사한다.

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)  # 원소의 개수

for i in range(1<<n):  # 1<<n : 부분 집합의 개수
		for j in range(n) :  # 원소의 수만큼 비트를 비교함
				if i & (1<<j) :  # i의 j번 비트가 1인 경우
						print(arr[j], end=", ")  # j번 원소 출력
		print()
print()
```

---

# 검색

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색 키 search key : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
    - 순차 검색 sequential search
    - 이진 검색 binary search
    - 해쉬 hash

<br>

## 순차 검색 sequential search

- 일렬로 되어 있는 자료를 순서대로 검색하는 경우
- 검색 대상의 수가 많은 경우 비효율적
- 정렬되어 있지 않은 경우 / 정렬되어 있는 경우(평균 비교 회수 절반)
- 시간 복잡도 : O(n)

<br>

## 이진 탐색 Binary Search

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 진행
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행
- **이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다**

### 검색 과정

- 자료의 중앙에 있는 원소를 고른다
- 중앙 원소의 값과 찾고자 하는 목표 값을 비교
- 목표값보다 중앙 원소 값이 작으면 자료의 왼쪽 반에서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행
- 찾고자 하는 값을 찾을 때까지 과정 반복

### 구현

- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.
- 이진 탐색의 경우, 자료의 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요

```python
def binarySearch (a, N, key):
		start = 0
		end = N-1
		while start <= end:
				middle = (start+end) // 2
				if a[middle] == key :  # 검색 성공
						return true
				elif a[middle] > key:
						end = middle - 1
				else:
						start = middle + 1
		return false  # 검색 실패
		
```

```python
# 재귀 함수 이용
def binarySearch (a, low, high, key):
		if low > high : # 검색 실패
				return False
		else:
				middle = (start+end) // 2
				if a[middle] == key :  # 검색 성공
						return true
				elif a[middle] > key:
						return binarySearch(a, low, middle-1, key)
				elif a[middle] < key:
						return binarySearch(a, middle+1, high, key)
```

---

# 인덱스

- Database에서 유래. 테이블의 동작 속도를 높여주는 자료 구조.
- 인덱스는 테이블보다 저장하는데 필요한 디스크 공간이 작다
- 대량의 데이터를 정렬하기보단 배열 인덱스를 이용하는 게 빠름!

<br>

---

# 선택 정렬 Selection Sort

- 주어진 자료 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

### 정렬 과정

- 주어진 리스트 중에서 최소값을 찾는다.
- 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
- 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

```python
def selectionSort(a, N):
		for i in range(N-1):
				minIdx = i
				for j in range(i+1, N):
						if a[minIdx] > a[j]:
								minIdx = j
				a[i], a[minIdx] = a[minIdx], a[i]
```

- 시간 복잡도 : O(n^2)

<br>

---

# 셀렉션 알고리즘 Selection Algorithm

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 최소값, 최대값, 중간값을 찾는 알고리즘

### 선택 과정

- 정렬 알고리즘을 이용하여 자료 정렬하기
- 원하는 순서에 있는 원소 가져오기

### k번째로 작은 원소를 찾는 알고리즘

- 1번부터 k번째까지 작은 원소들을 찾아 배열을 앞쪽으로 이동. 배열의 k번째를 반환
- 수행시간 : O(kn)

```python
def select(arr, k):
		for i in range(0, k):
				minIndex = i
				for j in range(i+1, len(arr)):
						if arr[minIndex] > arr[j]:
								minIndex = j
				arr[i], arr[minIndex] = arr[minIndex], arr[i]
		return arr[k-1]
```

<br>
