"""
9:06 시작
9:10 구상 완료
9:19 1차 구현 완료
"""


from collections import deque

N, K = map(int, input().split())
safety_lst = deque(map(int, input().split()))
ppl_lst = deque([0] * N)

turn = 0
while True:
    turn += 1
    # 한칸 회전한다
    ppl_lst.appendleft(ppl_lst.pop())
    safety_lst.appendleft(safety_lst.pop())

    # n-1번칸 확인
    ppl_lst[N - 1] = 0

    # 사람이 이동한다
    for i in range(N - 1)[::-1]:
        if ppl_lst[i]:  # 사람 있음
            if not (ppl_lst[i + 1] or safety_lst[i + 1] == 0):  # 이동 가능
                ppl_lst[i] = 0
                ppl_lst[i + 1] = 1
                safety_lst[i + 1] -= 1

    # n-1번칸 확인
    ppl_lst[N - 1] = 0

    # 0번칸에 사람 올린다
    if not (ppl_lst[0] or safety_lst[0] == 0):
        ppl_lst[0] = 1
        safety_lst[0] -= 1

    if safety_lst.count(0) >= K:
        break

print(turn)
