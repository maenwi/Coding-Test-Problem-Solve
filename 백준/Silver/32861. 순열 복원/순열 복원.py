import sys

def solution():
    input = sys.stdin.readline

    # 입력 받기
    N = int(input())
    # 행렬 입력 받기
    A = [list(map(int, input().split())) for _ in range(N)]
    # 복원할 원래 수열
    origin = list()

    # 혹시 행렬 대각원소가 0이 아니거나
    # 행렬이 대칭적이지 못한 경우
    for r in range(N):
        for c in range(r, N):
            if r == c and A[r][c] != 0:
                return None
            
            if r != c and A[r][c] != -A[c][r]:
                return None

    for a_row in A:
        number = 1
        for v in a_row:
            if v == -1:
                number += 1
    
        origin.append(str(number))

    if len(origin) != len(set(origin)):
        return None
    
    return origin

if __name__ == "__main__":
    origin = solution()
    if origin is None:
        print(-1)
    else:
        print(" ".join(origin))
