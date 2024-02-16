import sys

input = sys.stdin.readline

s = set()
N = int(input())
for _ in range(N):
    ipt = input()
    if ipt.startswith("add"):
        _, num = ipt.split()
        s.add(num)
    elif ipt.startswith("remove"):
        _, num = ipt.split()
        if num in s:
            s.remove(num)
    elif ipt.startswith("check"):
        _, num = ipt.split()
        if num in s:
            print(1)
        else:
            print(0)
    elif ipt.startswith("toggle"):
        _, num = ipt.split()
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif ipt.startswith("all"):
        s = set(map(str, range(1, 21)))
    elif ipt.startswith("empty"):
        s = set()
