N = int(input())
cranes = list(map(int, input().split()))

M = int(input())
boxes = list(map(int, input().split()))
box_aligned = [False for _ in range(M)]

def crane_and_box(cranes, boxes):
    cranes.sort(reverse=True) # 큰 -> 작
    boxes.sort(reverse=True) # 큰 -> 작

    # 가장 무거운 박스를, 가장 큰 크레인이 들 수 없으면
    if boxes[0] > cranes[0]: 
        return -1
    
    time = 0
    
    while boxes: # 모든 박스가 할당 될 때 까지
        time += 1 # 자 이게 작업 시작~
        crane_index = 0   # 맨 앞 크레인부터 업무 할당
        box_index = 0 # 맨 앞 박스부터 확인

        while crane_index < N and box_index < len(boxes):
            if cranes[crane_index] >= boxes[box_index]: # 크레인이 들 수 있으면
                boxes.pop(box_index) 
                crane_index += 1 
            else:
                box_index += 1 
                
        # 모든 크레인을 다 돌았다면?
        # 박스를 들 수 있는 크레인을 다 확인한거임
        # 따라서 다음으로 넘어감
    
    return time

print(crane_and_box(cranes, boxes))