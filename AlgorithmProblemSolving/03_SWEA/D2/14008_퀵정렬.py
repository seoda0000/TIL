'''
14008. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
'''
def qsort(lst):
    if len(lst) < 2:
        return lst
    # 1. pivot 을 기준으로 좌/우 나눔
    p = lst.pop()
    left = []
    right = []
    for n in lst:
        if n < p:
            left.append(n)
        else:
            right.append(n)

    # 2. 왼쪽 정렬, 오른쪽 정렬, 그 결과를 합쳐서 return
    return qsort(left) + [p] + qsort(right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = qsort(lst)
    print(f'#{tc}', lst[N//2])