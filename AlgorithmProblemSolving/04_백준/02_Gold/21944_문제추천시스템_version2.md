# 문제 추천 시스템 Version 2
https://www.acmicpc.net/problem/21944

tony9402는 최근 깃헙에 코딩테스트 대비 문제를 직접 뽑아서 "문제 번호, 난이도, 알고리즘 분류"로 정리해놨다.

깃헙을 이용하여 공부하시는 분들을 위해 새로운 기능을 추가해보려고 한다.

만들려고 하는 명령어는 총 3가지가 있다. 아래 표는 각 명령어에 대한 설명이다.

### recommend G x
x가 1인 경우 추천 문제 리스트에서 알고리즘 분류가 G인 문제 중 가장 어려운 문제 번호를 출력한다.  
조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 큰 것으로 출력한다.

x가 -1인 경우 추천 문제 리스트에서 알고리즘 분류가 G인 문제 중 가장 쉬운 문제 번호를 출력한다.  
조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 작은 것으로 출력한다.

해당 명령어는 해당 그룹 $G$에 문제 번호가 한 개 이상이 있을 경우에만 주어진다.

### recommend2 x
x가 1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 가장 어려운 문제 번호를 출력한다.  
조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 큰 것으로 출력한다.

x가 -1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 가장 쉬운 문제 번호를 출력한다.  
조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 작은 것으로 출력한다.

### recommend3 x L
x가 1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 난이도 L보다 크거나 같은 문제 중 가장 쉬운 문제 번호를 출력한다.  
조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 작은 것으로 출력한다. 만약 조건을 만족하는 문제 번호가 없다면 -1을 출력한다.

x가 -1인 경우 추천 문제 리스트에서 알고리즘 분류 상관없이 난이도 L보다 작은 문제 중 가장 어려운 문제 번호를 출력한다.  
조건을 만족하는 문제가 여러 개라면 그 중 문제 번호가 큰 것으로 출력한다. 만약 조건을 만족하는 문제 번호가 없다면 -1을 출력한다.


### add P L G	
추천 문제 리스트에 난이도가 L이고 알고리즘 분류가 G인 문제 번호 P를 추가한다. (추천 문제 리스트에 없는 문제 번호 $P$만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도와 다른 알고리즘 분류로 다시 들어 올 수 있다.)

### solved P
천 문제 리스트에서 문제 번호 P를 제거한다. (추천 문제 리스트에 있는 문제 번호 P만 입력으로 주어진다.)



명령어 recommend, recommend2, recommend3는 추천 문제 리스트에 문제가 하나 이상 있을 때만 주어진다.

명령어 solved는 추천 문제 리스트에 문제 번호가 하나 이상 있을 때만 주어진다.

위 명령어들을 수행하는 추천 시스템을 만들어보자.

---

## defaultdict 메서드
key의 기본값을 자동으로 설정하는 딕셔너리. 기본값은 int다.
값을 설정하지 않으면 value로 기본값이 호출된다.
* int : 0
* list : []
* dict : {}

```python
from collections import defaultdict
r1_dic = defaultdict(dict)
```


### 1. 입력 및 데이터형식

* recommend 명령어마다 defaultdict를 만든다.
* L과 P의 우선순위를 동시에 판단하기 위해 L에 1000000을 곱해 P와 더해준다.
  * P의 최대값 : 100000
* 문제 번호에 따라 난이도와 구분을 찾기 위해 problem_dic을 만들어준다.
```python
rank_prob = 1000000         # LLLPPPPPP 만드는 계수
N = int(input())
r1_dic = defaultdict(dict)  # recommend  : 우선순위 G > L > P     dic형식 {G:{LP:bool}}
r2_dic = defaultdict(dict)  # recommend2 : 우선순위 L > P         dic형식 {LP:bool}
r3_dic = defaultdict(dict)  # recommend3 : 우선순위 L > P > -1    dic형식 {L:{P:bool}}
prob_dic = dict()       # 전체 문제 dic : dic형식 {P:[L, G]}

for _ in range(N):
    P, L, G = map(int, input().split())
    calc_num = L * rank_prob + P    # LLLPPPPPP : 난이도와 문제 번호 합치기
    r1_dic[G][calc_num] = 1
    r2_dic[calc_num] = 1
    r3_dic[L][P] = 1
    prob_dic[P] = [L, G]
```

* 각 명령어마다 우선순위를 파악해 문제를 추천해준다.

```python
M = int(input())
for _ in range(M):
    command, *arg = input().split()

    if command == 'recommend':
        G, x = map(int, arg)
        if x > 0:
            calc_num = max(r1_dic[G].keys())    # G에 해당하는 가장 어려운 문제 (G에 해당하는 값중 -> L이 높고 -> P가 높은 것)
        else:
            calc_num = min(r1_dic[G].keys())    # G에 해당하는 가장 쉬운 문제 (G에 해당하는 값중 -> L이 낮고 -> P가 낮은 것)
        L = calc_num // rank_prob
        P = calc_num % rank_prob
        print(P)
    elif command == 'recommend2':
        x = int(arg[0])
        if x > 0:
            calc_num = max(r2_dic.keys())   # 가장 난이도가 높은 문제 중 문제 번호가 높은 것 (L이 크고 -> P가 큰 것)
        else:
            calc_num = min(r2_dic.keys())   # 가장 난이도가 낮은 문제 중 문제 번호가 낮은 것 (L이 낮고 -> P가 낮은 것)
        L = calc_num // rank_prob
        P = calc_num % rank_prob
        print(P)
    elif command == 'recommend3':
        x, target_L = map(int, arg)
        if x < 0:
            target_L = target_L - 1     # x가 -1인 경우 타겟 L보다 작아야 하므로 1을 빼준다.
        result = -1                     # 초기값 설정 (조건을 충족하는 문제가 없을 경우)
        while 0 <= target_L <= 100:
            if r3_dic.get(target_L):    # r3 dic에서 타겟 L 찾기
                if x > 0:
                    result = min(r3_dic[target_L].keys())   # 타겟 L보다 난이도가 같거나 어려운 문제 중 가장 쉬운 문제 (타겟 L보다 L이 같거나 크고 -> L이 작고 -> P가 낮은 것)
                else:
                    result = max(r3_dic[target_L].keys())   # 타겟 L보다 난이도가 쉬운 문제 중 가장 어려운 문제 (타겟 L보다 L이 작고 -> L이 크고 -> P가 높은 것)
                break
            target_L = target_L + x     # x가 양수인 경우 1을 더하고, x가 음수인 경우 1을 줄여야 한다.
        print(result)

    elif command == 'solved':
        P = int(arg[0])
        L, G = prob_dic[P]
        calc_num = L * rank_prob + P
        del r3_dic[L][P]            # 각 dic에서 값 제거
        del r2_dic[calc_num]
        del r1_dic[G][calc_num]
        
    else:                           # 명령어가 없는 경우 문제 추가
        P, L, G = map(int, arg)
        calc_num = L * rank_prob + P
        r1_dic[G][calc_num] = 1
        r2_dic[calc_num] = 1
        r3_dic[L][P] = 1
        prob_dic[P] = [L, G]
```



