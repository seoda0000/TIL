import sys

input = sys.stdin.readline


def check_alpha(nth, v_ladder):
    if nth >= K:  # 검증 완료
        return True

    cj = alpha_at_qi[nth]  # qi에서의 열
    success = False  # 사다리 성공 여부

    # 한번 내려가보기
    if go_down_from_qi(nth):
        success = True

    # 왼쪽 사다리 채워보기
    if not success and cj > 0:
        if not v_ladder[cj - 1]:  # 아직 확정 안 된 경우에만 채울 수 있다
            arr[qi][cj - 1] = ladder
            if go_down_from_qi(nth):
                success = True
            else:
                arr[qi][cj - 1] = blank

    # 오른쪽 사다리 채워보기
    if not success and cj < K - 1:
        if not v_ladder[cj]:  # 아직 확정 안 된 경우에만 채울 수 있다
            arr[qi][cj] = ladder
            if go_down_from_qi(nth):
                success = True
            else:
                arr[qi][cj] = blank

    if success:  # 성공 시 양옆 사다리 확정 후 다음으로
        if cj > 0: v_ladder[cj - 1] = 1
        if cj < K - 1: v_ladder[cj] = 1
        return check_alpha(nth + 1, v_ladder)
    else:  # 실패 시 바로 전체 불가능 처리
        return False


def go_down_from_qi(nth):  # qi에서 끝까지 내려가기

    cj = alpha_at_qi[nth]  # qi에서의 열

    for i in range(qi, N):  # 나머지 사다리 타기
        if cj < K - 1 and arr[i][cj] == ladder:  # 오른쪽 사다리 타기
            cj += 1
        elif cj > 0 and arr[i][cj - 1] == ladder:  # 왼쪽 사다리 타기
            cj -= 1

    # 마지막 위치가 타겟과 맞는지 확인
    if cj != target.index(chr(ord('A') + nth)):
        return False
    else:
        return True


blank, ladder = '*', '-'
K = int(input())
N = int(input())
target = input()
arr = [list(input()) for _ in range(N)]
qi = -1  # 문제의 사다리 행
for i in range(N):
    if '?' in arr[i]:
        qi = i
        arr[i] = [blank] * (K - 1)
        break

# 초기값 만들기
v_ladder = [0] * (K - 1)  # 사다리 확정 여부
alpha_at_qi = [0] * K  # 알파벳이 qi에서 어디에 위치하고 있는지
for j in range(K):  # j번째 알파벳이 qi에서 어디에 위치하고 있는지 체크
    cj = j  # 시작 열

    for i in range(N):  # qi까지 사다리 타기
        if i == qi:
            qj = cj
            alpha_at_qi[j] = cj
            break
        if cj < K - 1 and arr[i][cj] == ladder:  # 오른쪽 사다리 타기
            cj += 1
        elif cj > 0 and arr[i][cj - 1] == ladder:  # 왼쪽 사다리 타기
            cj -= 1

ans = 'x' * (K - 1)
if check_alpha(0, v_ladder):
    ans = ''.join(arr[qi])
print(ans)
