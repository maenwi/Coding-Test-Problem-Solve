from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리에는 트럭이 최대 bridge_length대 올라갈 수 있음.
    # 다리는 최대 weight까지의 무게를 견딜 수 있음.
    # 모든 트럭은 길이가 1, 1초에 bridge_length 1을 지날 수 있음.
    waits = deque(truck_weights) # 밑에서 대기 중인 트럭
    on_bridge = deque() # 다리 위에 올라와있는 트럭
    arrives = [] # 도착한 트럭

    time = 0

    while arrives != truck_weights:
        time += 1

        # 다리 위에 있는 트럭이 움직이고, 도착했으면 내려가기
        for i in range(len(on_bridge)):
            # 모든 트럭을 앞으로 한 칸 옮기고, bridge_length를 넘은 트럭만 내리자
            on_bridge[i][1] += 1
        
        if on_bridge and on_bridge[0][1] > bridge_length:
            arrives.append(on_bridge[0][0])
            weight += on_bridge[0][0]
            on_bridge.popleft()

        # 대기 중인 트럭이 다리 위로 올라가기
        # 다리가 견딜 수 있는 무게가 남아있고, 이번에 올라갈 차가 올라갈 공간이 있으면
        if waits and weight >= waits[0] and bridge_length >= len(on_bridge) + 1:
            # 올라가기
            going_on_truck = waits.popleft()
            weight -= going_on_truck
            on_bridge.append([going_on_truck, 1])

        # print(f"{arrives} | {on_bridge}, rw :{weight} | {waits}")

    return time