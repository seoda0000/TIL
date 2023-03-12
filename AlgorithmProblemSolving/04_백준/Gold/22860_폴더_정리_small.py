"""
폴더 정리 (small)
백준 골드3 22860
https://www.acmicpc.net/problem/22860

이름이 main 폴더 안에 여러가지 파일과 폴더가 존재한다.

main
 ├─ FolderA
 │    ├─ File1
 │    └─ File2
 └─ FolderB
       ├─ FolderC
       ├─ File1
       └─ File3
위 구조는 main 폴더의 하위 구조를 계층적으로 표시한 것이다. FolderA, FolderB, FolderC는 폴더이고 File1, File2, File3은 파일이다. 파일 이름이 같은 경우는 동일한 파일이다.

한 폴더 안에는 같은 이름의 파일이 두 개 이상 존재할 수 없다.

main 하위 디렉토리에 같은 이름의 폴더가 두 개 이상 존재할 수 없다.

폴더 정리를 하기 위해 main 폴더 하위에 있는 파일들을 확인하려고 한다.

주어지는 쿼리에 대해 폴더와 파일의 정보를 알려주는 프로그램을 만들어보자.
"""

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def findFile(f):
    global ans
    for fname in filetree[f]:
        child, id = fname
        if id == 0:
            ans += 1
            st.add(child)
        else:
            findFile(child)


N, M = map(int, input().split())
filetree = defaultdict(dict)
filetree['main'] = []

for _ in range(N+M):
    P, F, C = input().split()
    if P not in filetree:
        filetree[P] = [[F, int(C)]]
    else:
        filetree[P].append([F, int(C)])


Q = int(input())
for _ in range(Q):
    folder = input().rstrip().split('/')[-1]
    ans = 0
    st = set()
    findFile(folder)
    print(len(st), ans)


