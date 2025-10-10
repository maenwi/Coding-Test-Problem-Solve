from collections import deque

def solution(board):
    board = [list(s) for s in board]
    R, C = len(board), len(board[0])

    visited = [[False] * C for _ in range(R)]

    def roll(cur_r, cur_c, direction):
        dr, dc = [-1, +1, 0, 0], [0, 0, -1, +1]
        # 상하좌우
        
        # 이 while문은 장애물 혹은 벽 위치에 도달하고 끝나기 때문에
        while 0 <= cur_r < R and 0 <= cur_c < C and board[cur_r][cur_c] != "D":
            cur_r += dr[direction]
            cur_c += dc[direction]
        
        # 역방향으로 한 번 돌려주기
        cur_r -= dr[direction]
        cur_c -= dc[direction]

        return [cur_r, cur_c]
    
    # 시작 점 찾기
    for r in range(R):
        for c in range(C):
            if board[r][c] == "R":
                cur_r, cur_c = r, c
                board[r][c] = 0
            elif board[r][c] == ".":
                board[r][c] = 0
                # 또한 board에 그 지점까지 갈 수 있는 최단 구르기 횟수를 기록할거임

    q = deque([[cur_r, cur_c]])
    visited[cur_r][cur_c] = True
    
    while q:
        cur_r, cur_c = q.popleft()
    
        for direction in range(4):
            moved = roll(cur_r, cur_c, direction)
            # 네 방향으로 굴려보기
            
            if board[moved[0]][moved[1]] == "G":
                # 목적지에 도착했다면, 
                # 구르기 시작한 위치에서 구르기 횟수 + 1
                return board[cur_r][cur_c] + 1
            
            elif visited[moved[0]][moved[1]]: 
                # 움직인 지점을 이미 방문했었다면,
                #뭐 할게 없음
                continue 
                
            else: 
                # 목적지도 아니고 방문한 적도 없고, 방문 계획도 없는 경우에만
                q.append([moved[0], moved[1]])
                visited[moved[0]][moved[1]] = True
                board[moved[0]][moved[1]] = board[cur_r][cur_c] + 1

    return -1