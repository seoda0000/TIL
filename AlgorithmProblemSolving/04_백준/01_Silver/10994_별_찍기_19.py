"""
백준 10994
별 찍기 - 19
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""

import sys

N = int(sys.stdin.readline())
n = (N-1) * 4 + 1
ans = []
i = 0
start_even = ["*"] * n
start_odd = ["*"] + [" "] * (n-2) + ["*"]
even = []
odd = []
while i < (n+1)//2:
    if i % 2 == 0:
        if not even:
            even.append(start_even)
        else:
            target = even[-1][:]
            target[i-1] = " "
            target[-i] = " "
            even.append(target)
    else:
        if not odd:
            odd.append(start_odd)
        else:
            target = odd[-1][:]
            target[i - 1] = "*"
            target[-i] = "*"
            odd.append(target)
    i += 1

for j in range(len(even)):
    print("".join(even[j]))
    if len(odd) > j:
        print("".join(odd[j]))

for j in range(len(odd)-1, -1, -1):
    print("".join(odd[j]))
    print("".join(even[j]))


"""
1년 후 풀이
재귀 이용
"""

def draw(n):
    if n == 1:
        return ['*']
    else:
        bef = draw(n - 1)
        nb = len(bef)
        na = nb + 4
        arr = [
            "*" * na,
            "*" + " " * (na - 2) + "*",
        ]

        for i in range(nb):
            arr.append("* " + bef[i] + " *")
        arr += [
            "*" + " " * (na - 2) + "*",
            "*" * na,
        ]
        return arr

N = int(input())
arr = draw(N)
print(*arr, sep="\n")