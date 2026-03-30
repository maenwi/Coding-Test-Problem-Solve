import sys
import math

input = sys.stdin.readline

def solve():
    N = int(input())
    points = []
    for _ in range(N):
        a_point = input().split()
        points.append((
            float(a_point[0]),
            float(a_point[1]),
            float(a_point[2])
        ))
    # print(points)
    # 점 읽어오기
        
    # 초기 중심점: 모든 점의 무게중심(평균)
    cx = sum(p[0] for p in points) / N
    cy = sum(p[1] for p in points) / N
    cz = sum(p[2] for p in points) / N

    # print(f"{cx} {cy} {cz}")
    
    step = 0.1
    
    # Max Iteration 제한
    for _ in range(30000):
        max_dist_sq = -1.0
        max_p = points[0]
        
        # 중심 점 ~ 가장 먼 점 거리 (O(N))
        for p in points:
            dx = p[0] - cx
            dy = p[1] - cy
            dz = p[2] - cz
            dist_sq = dx*dx + dy*dy + dz*dz
            
            if dist_sq > max_dist_sq:
                max_dist_sq = dist_sq
                max_p = p
        
        # 가장 먼 점을 향해 이동
        cx += (max_p[0] - cx) * step
        cy += (max_p[1] - cy) * step
        cz += (max_p[2] - cz) * step
        
        # 이동 비율 조정
        step *= 0.999
        
    # 최종 반지름 계산
    ans_dist_sq = 0.0
    for p in points:
        dx = p[0] - cx
        dy = p[1] - cy
        dz = p[2] - cz
        dist_sq = dx*dx + dy*dy + dz*dz
        if dist_sq > ans_dist_sq:
            ans_dist_sq = dist_sq
            
    ans = math.sqrt(ans_dist_sq)
    
    print(f"{ans:.2f}")

if __name__ == '__main__':
    solve()