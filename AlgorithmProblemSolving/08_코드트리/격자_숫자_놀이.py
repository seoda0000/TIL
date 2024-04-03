"""
9:50 시작
9:54 구상 완료
10:06 1차 구현 완료
10:14 디버깅 완료 (input 좌표에서 1 안 뺌)
"""


def get_new_arr(arr, N, M):
    newM = 0
    for i in range(N):
        row = arr[i]

        num_lst = list(set(row) - {0})
        tup_lst = []

        for num in num_lst:
            tup_lst.append((num, row.count(num)))
        tup_lst.sort(key=lambda x: (x[1], x[0]))

        new_row = []
        for tup in tup_lst:
            new_row.append(tup[0])
            new_row.append(tup[1])

        newM = max(newM, len(new_row))
        new_row += [0] * (100 - len(new_row))
        arr[i] = new_row[:100]

    return arr, N, newM


I, J, K = map(int, input().split())
I-=1
J-=1
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    arr[i][:3] = list(map(int, input().split()))

N = M = 3
t = 0
while True:

    if arr[I][J] == K:
        break

    if N >= M:
        arr, N, M = get_new_arr(arr, N, M)
    else:
        arr, M, N = get_new_arr(list(map(list, zip(*arr))), M, N)
        arr = list(map(list, zip(*arr)))

    t += 1
    if t > 100:
        t = -1
        break

print(t)
