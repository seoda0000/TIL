N = int(input())
lst = []
for n in range(N):
    age, name = input().split()
    lst.append((int(age), name, n))

lst.sort(key=lambda x:(x[0], x[2]))
for l in lst:
    print(*l[:2])
