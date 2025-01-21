# 대칭이동의 idea
def solution(m, n, startX, startY, balls):
    
    def flip(side, ball):
        if side == "left":
            return [-ball[0], ball[1]]
        elif side == "top":
            return [ball[0], (n - ball[1]) + n]
        elif side == "right":
            return [(m - ball[0]) + m, ball[1]]
        elif side == "bottom":
            return [ball[0], -ball[1]]

    def dist(ball1, ball2):
        return (ball1[0] - ball2[0])**2 + (ball1[1] - ball2[1])**2
    
    answer = []
    flip_side = ["left", "top", "right", "bottom"]
    for ball in balls:
        min_dist = m ** 2 + n ** 2
        for fs in flip_side:
            if ball[1] == startY:
                if ball[0] < startX and fs == "left":
                    # 공이 같은 y좌표에 있고, 내가 칠 공이 더 왼쪽에 있고, 대칭이동이 오른쪽 사이드임.
                    # 그러면 대칭이동 할 필요 없음
                    continue
                elif ball[0] > startX and fs == "right":
                    continue
            elif ball[0] == startX:
                if ball[1] < startY and fs == "bottom":
                    # 공이 같은 x좌표에 있고, 내가 칠 공이 더 위에 있고,
                    # 대칭이동이 아래 사이드이면, 대칭이동 필요 없음
                    continue
                elif ball[1] > startY and fs == "top":
                    continue
            
            # 공 대칭이동
            fliped_ball = flip(fs, ball)
            d = dist(fliped_ball, [startX, startY])
            if d <= min_dist:
                min_dist = d
        answer.append(min_dist)
    return answer