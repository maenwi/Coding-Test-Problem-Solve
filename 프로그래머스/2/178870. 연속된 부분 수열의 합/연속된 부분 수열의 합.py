from collections import deque

def solution(sequence, k):
    # if k in sequence:
    #     return [sequence.index(k), sequence.index(k)]
    
    answer = deque()
    answer_list = []
    summation = 0
    for i, s in enumerate(sequence):
        summation += s
        answer.append(s)
        
        #내가 위에서 원소를 추가했는데
        #k보다 커졌어 그러면 맨 앞 원소부터 하나씩 빼줘야함
        while summation > k:
            imsi = answer.popleft() #그럼 앞에꺼를 빼주고
            summation -= imsi #summation에서 빼준 값 빼줌
            #아직 summation > k라면 또 빼줄거임
        
        if summation == k:
            #while문이 끝났으며, 원하는 부분 수열이 만들어진 경우
            answer_list.append([i-len(answer) + 1,i])
            #아래는 이제 다음 부분 수열을 찾기 위함
            imsi = answer.popleft()
            summation -= imsi
        
        # 만약 while문이 끝나서, summation <= k가 됐지만
        # 아직 summation == k는 안된 경우
    
    answer_list.sort(key = lambda x: (x[1]-x[0]+1, x[0]))
            
    return answer_list[0]