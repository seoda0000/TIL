'''
[파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 (제출용) D3

알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.





정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.
'''


def merge_sort(lst):
    global cnt
    if len(lst) < 2: # 정렬대상이 1개이면 종료
        return lst

    m = len(lst)//2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    if left[-1] > right[-1]:  # 정답 구하기
        cnt += 1

    f1 = f2 = 0
    tmp = []
    while f1 < len(left) and f2 < len(right):
        if left[f1] < right[f2]:
            tmp.append(left[f1])
            f1 += 1
        else:
            tmp.append(right[f2])
            f2 += 1
    tmp += left[f1:] + right[f2:]
    return tmp


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f'#{tc}', lst[N//2], cnt)
