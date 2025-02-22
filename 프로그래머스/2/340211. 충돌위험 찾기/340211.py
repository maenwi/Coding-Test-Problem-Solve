# https://school.programmers.co.kr/learn/courses/30/lessons/340211

def move(points, start_node_index, end_node_index):
    s = points[start_node_index][:]
    e = points[end_node_index][:] 

    go_down = s[0] <= e[0]  # True: 아래로, False: 위로
    go_right = s[1] <= e[1]  # True: 오른쪽으로, False: 왼쪽으로

    trail = []

    while s[0] != e[0]:
        if go_down:
            s[0] += 1
        else:
            s[0] -= 1
        trail.append([s[0], s[1]])

    while s[1] != e[1]:
        if go_right:
            s[1] += 1
        else:
            s[1] -= 1
        trail.append([s[0], s[1]])

    return trail

def solution(points, routes):
    points = [[]] + points
    
    robot_trails = []
    max_moves = -1 # 어느 로봇이 가장 오래 이동했는지

    for route in routes:
        temp_route_trails = [points[route[0]]]
        
        for i in range(len(route) - 1):
            temp_route_trails += move(points, route[i], route[i + 1])
        
        moves = len(temp_route_trails)
        if moves >= max_moves:
            max_moves = moves

        robot_trails.append(temp_route_trails)
    
    crash = 0
    for t in range(max_moves):
        locations = []
        crashed_location = []
        for robot in range(len(routes)):
            # 리스트 인덱싱을 try except로 해결
            try:
                current = robot_trails[robot][t]
            except:
                current = [-1, -1]
            
            if current in locations: #이미 여기에 있는 로봇이 있다면
                if current not in crashed_location and current != [-1, -1]:
                    crash += 1
                    crashed_location.append(current)
                
            else:
                locations.append(current)
    
    return crash